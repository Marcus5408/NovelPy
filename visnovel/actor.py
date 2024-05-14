from math import e
from typing import Dict, Union, List
import os

class EmotionState():
    def __init__(self, emotion: str, image_path: int) -> None:
        self.emotion = emotion
        # check if image_path is a valid path
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Attempted to define {emotion} as {image_path}, which does not exist.")
        else:
            self.image_path = image_path

class Character:
    def __init__(self, name: str, emotion_states: List[EmotionState], default_emotion: str) -> None:
        self.name = name
        self.emotions = {}
        for emotion in emotion_states:
            if emotion.emotion in self.emotions:
                raise KeyError(f"Attempted to define {emotion.emotion} twice for {self.name}.")
            else:
                self.emotions[emotion.emotion] = emotion.image_path
        
        try:
            self.emotions["default"] = self.emotions[default_emotion]
        except KeyError:
            raise KeyError(f"Attempted to define {self.name}'s default emotion as '{default_emotion}', which does not exist.")

class Actor:
    def __init__(self, name: str, emotions: List[EmotionState]) -> None:
        self.name = name
        self.emotions = emotions
        self.current_emotion = None
    
    def set_emotion(self, emotion: str) -> str:
        if emotion not in self.emotions:
            raise KeyError(f"{emotion} not found in emotions.")
        else:
            return self.emotions[emotion]