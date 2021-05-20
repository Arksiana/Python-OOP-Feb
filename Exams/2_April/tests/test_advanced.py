import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    name = 'Player'

    def setUp(self):
        self.player = Advanced(self.name)

    def test_check_attr_are_set(self):
        self.assertEqual(self.name, self.player.username)
if __name__ == '__main__':
    unittest.main()
