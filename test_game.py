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


if __name__ == '__main__':
    unittest.main()
