import pygame as pg
import typing

class Pytale:
    def __init__(self, screen_size: tuple[int, int], title: str) -> None:
        pg.init()
        self.screen = pg.display.set_mode(screen_size)
        pg.display.set_caption(title)

    def run(self) -> None:
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.screen.fill((0, 0, 0))
            pg.display.flip()
        pg.quit()