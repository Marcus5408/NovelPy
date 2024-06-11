import pygame as pg
from typing import List, Tuple
import os


class Character:
    def __init__(
        self, name: str, states: List[dict], default: str
    ) -> None:
        self.name = name
        self.emotions = {}
        for emotion in states:
            if emotion["emotion"] in self.emotions:
                raise KeyError(
                    f"Attempted to define {emotion.emotion} twice for {self.name}."
                )
            else:
                self.emotions[emotion["emotion"]] = emotion["image_path"]

                # Define a new function for this emotion
                def emotion_func(self, emotion=emotion["emotion"]):
                    # create pygame surface
                    surface = pg.image.load(self.emotions[emotion])
                    # resize the surface
                    # surface = pg.transform.scale(surface, size)
                    # display the surface
                    self.screen.blit(surface, (0, 0))

                # Assign the function as an attribute of this instance
                setattr(self, emotion["emotion"], emotion_func.__get__(self))

        try:
            self.emotions["default"] = self.emotions[default]
        except KeyError:
            raise KeyError(
                f"Attempted to define {self.name}'s default emotion as '{default}', which does not exist."
            )

    def __str__(self) -> str:
        return self.name
