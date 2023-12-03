import unittest

from classes.n_dimensional_grid import NDimensionalGrid
from classes.priority_queue import PriorityQueue


class NDimensionalGridTests(unittest.TestCase):
    def test_get(self):
        grid = NDimensionalGrid(dimensions=2)
        self.assertEqual(grid.get(0, 0), None)

        grid = NDimensionalGrid(dimensions=3, default=lambda: ".")
        self.assertEqual(grid.get(1, 6, 3), ".")

    def test_get_adjacent(self):
        grid = NDimensionalGrid(dimensions=2, default=lambda: False)
        grid.set(1, 1, value=True)

        self.assertDictEqual(
            grid.get_adjacent(0, 0, include_diagonal=True),
            {
                (-1, -1): False,
                (0, -1): False,
                (1, -1): False,
                (1, 0): False,
                (1, 1): True,
                (0, 1): False,
                (-1, 1): False,
                (-1, 0): False,
            },
        )

        self.assertDictEqual(
            grid.get_adjacent(2, 1, include_diagonal=False),
            {
                (1, 1): True,
                (3, 1): False,
                (2, 0): False,
                (2, 2): False,
            },
        )


class PriorityQueueTests(unittest.TestCase):
    def test_add_item(self):
        queue = PriorityQueue()
        self.assertEqual(len(queue), 0)

        added_item = queue.add_item("foo", 1)
        self.assertListEqual(list(queue), ["foo"])
        self.assertEqual(added_item, "foo")

        queue.add_item("bar", 2)
        self.assertListEqual(list(queue), ["bar", "foo"])

        queue.add_item(42, 0)
        self.assertListEqual(list(queue), ["bar", "foo", 42])

    def test_is_empty(self):
        queue = PriorityQueue()
        self.assertTrue(queue.is_empty())

        queue.add_item("foo", 1)
        self.assertFalse(queue.is_empty())

        queue.pop()
        self.assertTrue(queue.is_empty())

    def test_pop(self):
        queue = PriorityQueue()
        queue.add_item("foo", 1)
        queue.add_item("bar", 2)
        queue.add_item(42, 0)

        self.assertEqual(queue.pop(), 42)
        self.assertEqual(queue.pop(), "foo")
        self.assertEqual(queue.pop(), "bar")
        self.assertTrue(queue.is_empty())
