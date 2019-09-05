import unittest

from Game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()


class TestGameRoll(TestGame):
    def test_negative_pins_given(self):
        self.assertRaises(ValueError, lambda: self.game.roll(-1))

    def test_more_than_ten_pins(self):
        self.assertRaises(ValueError, lambda: self.game.roll(11))

    def test_increase_rolls(self):
        initial_rolls = self.game.current_roll
        self.game.roll(7)
        self.assertEqual((initial_rolls + 1), self.game.current_roll)

    def test_rolls_not_more_than_two(self):
        self.game.roll(4)
        self.game.roll(4)
        self.game.roll(4)
        self.assertLess(self.game.current_roll, 3)

    def test_increase_number_frames(self):
        initial_frames = self.game.current_frames
        self.game.roll(4)
        self.game.roll(4)
        self.assertEqual((initial_frames + 1), self.game.current_frames)

    def test_increase_pins_knocked_down_after_roll(self):
        initial_pins = self.game.pins_knocked_down
        self.game.roll(4)
        self.assertEqual((initial_pins + 4), self.game.pins_knocked_down)


if __name__ == '__main__':
    unittest.main()
