import pygame as pg
from typing import Dict
from act import *
from character import *
import ulid


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
        self.game_queue = []
        self.current_queue = []
        self.rendered_queue = []
        self.text_screen(bg=(0, 0, 0), name="")

    def mainloop(self) -> None:
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()

            if self.game_queue != self.rendered_queue:
                for action in self.game_queue:
                    if action["ulid"] not in [
                        current_action["ulid"] for current_action in self.current_queue
                    ]:
                        self.current_queue.append(action)

                for action in self.current_queue:
                    if action["time_started"] is not None:
                        if (
                            pg.time.get_ticks() - action["time_started"]
                            > action["duration"] * 1000
                        ):
                            action = None
                    self.screen.blit(action["surface"], (0, 0))
                    action["time_started"] = (
                        pg.time.get_ticks()
                        if action["time_started"]
                        else action["time_started"]
                    )
                    pg.display.flip()
                self.current_queue = [
                    action for action in self.current_queue if action is not None
                ]

                # remove actions that have expired from game_queue
                self.game_queue = []
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
                "ulid": ulid.new(),
                "surface": screen_copy,
                "duration": duration,
                "time_started": None,
            }
        )

    def character_screen(self):
        pass


if __name__ == "__main__":
    config = {
        "screen_size": (800, 600),
        "title": "Adventure Novel",
    }
    vn = VisNovel(config)
    alice = Character(
        name="Alice",
        states=[
            {"emotion": "happy", "image_path": "example/alice_happy.png"},
            {"emotion": "sad", "image_path": "example/alice_sad.png"},
        ],
        default="happy",
    )
    bob = Character(
        name="Bob",
        states=[
            {"emotion": "happy", "image_path": "example/bob_happy.png"},
            {"emotion": "sad", "image_path": "example/bob_sad.png"},
        ],
        default="happy",
    )
    vn.text_screen(name="Act 1", duration=5)
    vn.scene(bg="example/bg.png", characters=[alice, bob])
    vn.mainloop()
