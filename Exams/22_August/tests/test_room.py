import unittest

from project.people.child import Child
from project.rooms.room import Room


class TestCaseBase(unittest.TestCase):
    def assertListEmpty(self, ll):
        self.assertListEqual([], ll)


class TestRooms(TestCaseBase):
    name = 'Roomname'
    budget = 123
    members_count = 4

    def setUp(self):
        self.room = Room(self.name, self.budget, self.members_count)

    def test_check_attr_are_set(self):
        self.assertEqual(self.name, self.room.family_name)
        self.assertEqual(self.budget, self.room.budget)
        self.assertEqual(self.members_count, self.room.members_count)
        self.assertListEmpty(self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_when_expenses_is_negative__expect_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = - 5
        self.assertEqual('Expenses cannot be negative', str(ex.exception))

    def test_when_expenses_is_positive_expect_to_set(self):
        self.room.expenses = 5
        self.assertEqual(5, self.room.expenses)

    def test_when_expenses_is_0_expect_to_set(self):
        self.room.expenses = 0
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses_when_zero_consumes_expect_expenses_to_be_0(self):
        self.room.calculate_expenses([])
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses_when_one_consumes_expect_expenses_to_be_correct(self):
        consumers = [Child(1, 2, 3, 4)]
        self.room.calculate_expenses(consumers)
        self.assertEqual(consumers[0].get_monthly_expense(), self.room.expenses)

    def test_calculate_expenses_when_two_consumes_expect_expenses_to_be_correct(self):
        appliances = [Child(1, 2, 3, 4)]
        children = [Child(5, 1, 2, 3)]
        self.room.calculate_expenses(appliances, children)
        expected = appliances[0].get_monthly_expense() + children[0].get_monthly_expense()
        self.assertEqual(expected, self.room.expenses)


if __name__ == '__main__':
    unittest.main()
