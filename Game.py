class Game:

    def __init__(self):
        self.frames = 10
        self.rolls = 2
        self.current_roll = 1
        self.pins = 10
        self.pins_knocked_down = 0
        self.strikes = 0
        self.spares = 0

    def roll(self, pins):
        if pins < 0:
            raise ValueError("Please enter valid number of pins. Negative number entered")

        if pins > 10:
            raise ValueError("Please enter valid number of pins. More than 10 entered")

        if self.current_roll == 2:
            self.current_roll = 1
        else:
            self.current_roll += 1
