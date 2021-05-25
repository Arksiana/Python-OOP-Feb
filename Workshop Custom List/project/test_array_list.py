from unittest import TestCase

from project.array_list import ArrayList


class TestArrayList(TestCase):
    def test_append_when_list_is_empty_expect_append_to_the_end(self):
        al = ArrayList()
        al.append(1)
        values = list(al)

        self.assertEqual([1], values)

    def test_append_when_list_not_empty_expect_append_to_the_end(self):
        al = ArrayList()
        al.append(1)
        al.append(2)
        al.append(3)
        values = list(al)
        self.assertEqual([1, 2, 3], values)

    

