import unittest

from project.battle_field import BattleField
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattle(unittest.TestCase):
    def setUp(self):
        self.battle_field = BattleField()

    def test_attacker_is_beginner_without_cards_should_increase_health_point(self):
        attacker = Beginner('attacker')
        enemy = Advanced('enemy')

        self.battle_field.fight(attacker, enemy)
        self.assertEqual(90, attacker.health)
        self.assertEqual(250, enemy.health)

if __name__ == '__main__':
    unittest.main()
