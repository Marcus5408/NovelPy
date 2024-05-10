import unittest
from pytale.actor import EmotionState, Character, Actor

class TestActorModule(unittest.TestCase):
    def setUp(self):
        self.emotion1 = EmotionState("happy", "/valid/path/to/image")
        self.emotion2 = EmotionState("sad", "/valid/path/to/image")
        self.character = Character("John", [self.emotion1, self.emotion2])
        self.actor = Actor("John", [self.emotion1, self.emotion2])

    def test_emotion_state(self):
        with self.assertRaises(FileNotFoundError):
            EmotionState("angry", "/invalid/path/to/image")
        self.assertEqual(self.emotion1.emotion, "happy")
        self.assertEqual(self.emotion1.image_path, "/valid/path/to/image")

    def test_character(self):
        with self.assertRaises(KeyError):
            Character("John", [self.emotion1, self.emotion1])
        with self.assertRaises(KeyError):
            Character("John", [self.emotion2])
        self.assertEqual(self.character.name, "John")
        self.assertEqual(self.character.emotions, {"happy": "/valid/path/to/image", "sad": "/valid/path/to/image"})

    def test_actor(self):
        self.assertEqual(self.actor.name, "John")
        self.assertEqual(self.actor.emotions, [self.emotion1, self.emotion2])
        self.assertIsNone(self.actor.current_emotion)
        with self.assertRaises(KeyError):
            self.actor.set_emotion("angry")
        self.assertEqual(self.actor.set_emotion("happy"), "/valid/path/to/image")

if __name__ == "__main__":
    unittest.main()