class Game:

    def __init__(self):
        self.frames = 10
        self.current_frames = 1
        self.rolls = 2
        self.current_roll = 1
        self.pins = 10
        self.pins_knocked_down = 0
        self.pins_knocked_down_in_frame = 0
        self.strikes = False
        self.strikes_bonus = 0
        self.spares = False
        self.spares_bonus = 0

    def roll(self, pins):
        if pins < 0:
            raise ValueError("Please enter valid number of pins. Negative number entered")

        if pins > 10:
            raise ValueError("Please enter valid number of pins. More than 10 entered")

        if (self.pins_knocked_down_in_frame + pins) > 10:
            raise ValueError("You can not enter more than 10 pins per frame")

        if self.spares:
            self.spares_bonus += pins
            self.spares = False

        if self.current_roll == 1 and pins == 10:
            self.current_roll = 2

        self.pins_knocked_down_in_frame += pins
        self.pins_knocked_down += pins

        if self.pins_knocked_down_in_frame == 10:
            self.spares = True

        if self.current_roll == 2:
            self.current_roll = 1
            self.current_frames += 1
            self.pins_knocked_down_in_frame = 0
        else:
            self.current_roll += 1
