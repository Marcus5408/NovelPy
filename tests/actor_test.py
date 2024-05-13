import unittest
from visnovel.actor import EmotionState, Character, Actor

class TestActorModule(unittest.TestCase):
    def setUp(self):
        self.emotion1 = EmotionState("happy", "tests/test.jpg")
        self.emotion2 = EmotionState("sad", "tests/test.jpg")
        self.character = Character("John", [self.emotion1, self.emotion2])
        self.actor = Actor("John", [self.emotion1, self.emotion2])

    def test_emotion_state(self):
        with self.assertRaises(FileNotFoundError):
            EmotionState("angry", "/invalid/path/to/image")
        self.assertEqual(self.emotion1.emotion, "happy")
        self.assertEqual(self.emotion1.image_path, "tests/test.jpg")

    def test_character(self):
        with self.assertRaises(KeyError):
            Character("John", [self.emotion1, self.emotion1])
        with self.assertRaises(KeyError):
            Character("John", [self.emotion2])
        self.assertEqual(self.character.name, "John")
        self.assertEqual(self.character.emotions, {"happy": "tests/test.jpg", "sad": "tests/test.jpg"})

    def test_actor(self):
        self.assertEqual(self.actor.name, "John")
        self.assertEqual(self.actor.emotions, [self.emotion1, self.emotion2])
        self.assertIsNone(self.actor.current_emotion)
        with self.assertRaises(KeyError):
            self.actor.set_emotion("angry")
        self.assertEqual(self.actor.set_emotion("happy"), "tests/test.jpg")

if __name__ == "__main__":
    unittest.main()