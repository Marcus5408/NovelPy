from . import visnovel as vn

class Game(vn.Game):
    def __init__(self):
        super().__init__(window_name="Example", window_size=(800, 600), window_favicon="tests/test.jpg")
        self.start()

    def start(self):
        self.actor = vn.Actor("John", ["tests/test.jpg", "tests/test.jpg"], "happy")
        self.actor.speak("Hello, world!")
    
    class Act1(vn.Act):
        def __init__(self):
            super().__init__(title="Act 1", subtitle="This is the first act")
        
        def effect(self, actor, target):
            actor.speak("Act 1 effect")