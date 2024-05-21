import pygame as pg
import typing
from act import *
from character import *
import threading


class VisNovel:
    def __init__(self, screen_size: tuple[int, int], title: str) -> None:
        pg.init()
        self.screen = pg.display.set_mode(screen_size)
        pg.display.set_caption(title)
        self.running = True
        self.run()

    def run(self) -> None:
        self.running = True
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            pg.display.flip()
        pg.quit()

    def title(self, h1: str, h2: str, h3: str, bg: str, duration: int) -> None:
        # add title to screen



if __name__ == "__main__":
    visnovel = VisNovel(screen_size=(800, 600), title="Adventure Novel")
    scene = visnovel.Scene(name="Act 1")
    scene.run()