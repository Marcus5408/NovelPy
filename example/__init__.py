import novelpy as pt

class Example:
    def __init__(self):
        self.name = "Example"
        self.description = "This is an example game"
        self.version = "0.0.1"

    def run(self):
        pt.run(self.name, self.description, self.version)

if __name__ == "__main__":
    Example().run()