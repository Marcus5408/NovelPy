import typing


class Act:
    def __init__(self, name: str, description: str, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def execute(self, actor, target):
        self.effect(actor, target)
