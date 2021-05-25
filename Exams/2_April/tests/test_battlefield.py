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


    def test_enemy_is_beginner_should_increase_health_points(self):
        attacker = Advanced('attacker')
        enemy = Beginner('enemy')

        self.battle_field.fight(attacker, enemy)
        self.assertEqual(250, attacker.health)
        self.assertEqual(90, enemy.health)

    def test_attacker_is_dead_should_raise_exception(self):
        attacker = Beginner('attacker')
        enemy = Advanced('enemy')

        attacker.health = 0

        with self.assertRaises(ValueError) as context:
            self.battle_field.fight(attacker, enemy)

        self.assertEqual(str(context.exception), 'Player is dead!')

    def test_enemy_is_dead_should_raise_exception(self):
        attacker = Advanced('attacker')
        enemy = Advanced('enemy')

        enemy.health = 0

        with self.assertRaises(ValueError) as context:
            self.battle_field.fight(attacker, enemy)

        self.assertEqual(str(context.exception), 'Player is dead!')




if __name__ == '__main__':
    unittest.main()
