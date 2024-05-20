from . import visnovel as vn
from .visnovel import *

# create characters

alice = vn.Character(name="Alice", emotions=[
    {
        "emotion": "happy",
        "image_path": "example/alice_happy.png"
    },
    {
        "emotion": "sad",
        "image_path": "example/alice_sad.png"
    }
], default="happy")

bob = vn.Character(name="Bob", emotions=[
    {
        "emotion": "happy",
        "image_path": "example/bob_happy.png"
    },
    {
        "emotion": "sad",
        "image_path": "example/bob_sad.png"
    }
], default="happy")

vn.init(screen_size=(800, 600), title="Adventure Novel")
vn.title(h1="Adventure Novel", h2="A Visual Novel Engine in Python", h3="By Your Name Here", bg="example/bg.png", duration=10)
vn.scene(name="Act 1", bg="example/bg.png", characters=[alice, bob])
vn.narrator(text="Once upon a time, in a land far, far away...", duration=5)
vn.dialogue(character=alice, text="Hello, Bob!")
vn.dialogue(character=bob, text="Hello, Alice!")
vn.dialogue(character=alice, text="How are you today?")
vn.choice(character=bob, text="I'm happy!", choices=[
    {
        "text": "That's great!",
        "effect": lambda: bob.happy()
    },
    {
        "text": "That's not great.",
        "effect": lambda: bob.sad()
    }
])