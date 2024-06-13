from tracemalloc import start
import pygame as pg
from typing import Dict, Union
from scene import *
from character import *
import gamequeue as gq


class VisNovel:
    def __init__(self, configs: Dict) -> None:
        #  screen_size: tuple[int, int], title: str
        self.config = configs
        pg.init()
        default_font = f"{__file__.replace('__init__.py', '')}Roboto-Regular.ttf"
        self.config["default_font"] = (
            self.config["default_font"]
            if "default_font" in self.config
            else default_font
        )
        self.default_font = pg.font.Font(self.config["default_font"], 32)
        self.screen = pg.display.set_mode(self.config["screen_size"])
        pg.display.set_caption(self.config["title"])
        self.running = True
        self.game_queue = gq.GameQueue()
        self.text_screen(bg=(0, 0, 0), name="")

    class RenderableObject:
        def __init__(self, duration):
            self.duration = duration
            self.start_time = pg.time.get_ticks()

        def isActive(self):
            return pg.time.get_ticks() - self.start_time < self.duration

    def mainloop(self) -> None:
        start = pg.time.get_ticks()
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()

            if not self.game_queue.is_empty():
                current = self.game_queue.peek()
                if current["time_started"] is 0:
                    current["time_started"] = pg.time.get_ticks()
                elif pg.time.get_ticks() - current["time_started"] > current["duration"]:
                    self.game_queue.remove()
                pg.display.flip()

    def text_screen(
        self,
        bg: tuple[int, int, int] = (0, 0, 0),
        name: str = "Act 1",
        duration: int = 5,
    ) -> None:
        # create new surface the size of screen
        screen_copy = self.screen.copy()
        screen_copy.fill(bg)
        text = self.default_font.render(name, True, (255, 255, 255))
        text_rect = text.get_rect()
        # center the text
        text_rect.center = (
            self.config["screen_size"][0] // 2,
            self.config["screen_size"][1] // 2,
        )
        # blit the text onto the screen
        screen_copy.blit(text, text_rect)
        self.game_queue.append(
            {
                "type": "TextScreen",
                "surface": screen_copy,
                "duration": duration,
                "time_started": 0,
            }
        )

    def scene(
        self,
        bg: Union[tuple[int, int, int], str] = (0, 0, 0),
        characters: List[Character] = [],
    ) -> None:
        # create new surface the size of screen
        screen_copy = self.screen.copy()
        if isinstance(bg, str):
            bg = pg.image.load(bg)
            bg = pg.transform.scale(bg, self.config["screen_size"])
            screen_copy.blit(bg, (0, 0))
        else:
            screen_copy.fill(bg)

        for character in characters:
            # scale character image to screen size
            character.emotions = {
                key: pg.transform.scale(
                    pg.image.load(value),
                    (
                        int(self.config["screen_size"][1]
                            * pg.image.load(value).get_width()
                            // pg.image.load(value).get_height()),
                        self.config["screen_size"][1]
                    ),
                )
                for key, value in character.emotions.items()
            }
            # calculate position: character index in characters param // width of screen
            x = (
                characters.index(character)
                * self.config["screen_size"][0]
                // len(characters)
            )
            # load character image
            print(character.emotions["default"])
            screen_copy.blit(character.emotions["default"], (x, 0))

        self.screen.blit(screen_copy, (0, 0))
        # self.game_queue.append(
        #     {
        #         "type": "Scene",
        #         "surface": screen_copy,
        #         "duration": 0,
        #         "time_started": None,
        #     }
        # )

    def play_audio(
        self,
        audio_path: str,
        duration: int,
    ) -> None:
        # create new surface the size of screen
        screen_copy = self.screen.copy()
        screen_copy.fill((0, 0, 0))
        self.game_queue.append(
            {
                "type": "Audio",
                "audio_path": audio_path,
                "duration": duration,
                "time_started": None,
            }
        )
        return None


if __name__ == "__main__":
    config = {
        "screen_size": (800, 600),
        "title": "Doki Doki No Club :(",
    }
    vn = VisNovel(config)
    monika = Character(
        name="Monika",
        states=[
            {"emotion": "happy", "image_path": "visnovel/monika_happy.png"},
            {"emotion": "sad", "image_path": "visnovel/monika_sad.png"},
        ],
        default="happy",
    )
    monika2 = Character(
        name="Monika2",
        states=[
            {"emotion": "happy", "image_path": "visnovel/monika_happy.png"},
            {"emotion": "sad", "image_path": "visnovel/monika_sad.png"},
        ],
        default="sad",
    )
    vn.text_screen(name="Act 1", duration=5)
    vn.scene(bg="visnovel/bg/class.png", characters=[monika, monika2])
    vn.mainloop()
