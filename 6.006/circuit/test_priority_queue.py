import unittest
from priority_queue_2 import PriorityQueue


class TestPriorityQueye(unittest.TestCase):
    #@unittest.skip("demonstrating skipping")
    def test_append(self):
        queue = PriorityQueue()
        self.assertEqual(0, len(queue), "length of empty queue should be 0")

        queue.append(1)
        self.assertEqual(1, len(queue))

        queue.append(1)
        self.assertEqual(2, len(queue))

        queue.append(2)
        self.assertEqual(3, len(queue))

    #@unittest.skip("demonstrating skipping")
    def test_min(self):
        queue = PriorityQueue()
        self.assertIsNone(queue.min())

        queue.append(10)
        self.assertEqual(10, queue.min())

        queue.append(15)
        self.assertEqual(10, queue.min())

        queue.append(20)
        self.assertEqual(10, queue.min())

        queue.append(5)
        self.assertEqual(5, queue.min())

        queue.append(10)
        self.assertEqual(5, queue.min())
        self.assertEqual(5, len(queue))

    # @unittest.skip("demonstrating skipping")
    def test_pop_2(self):
        lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        queue = PriorityQueue()
        for i in lst:
            queue.append(i)

        for i in reversed(lst):
            min_value = queue.pop()
            self.assertEqual(i, min_value)

        self.assertIsNone(queue.pop())
        self.assertIsNone(queue.min())

    def test_pop_3(self):
        lst = [10, 9, 8, 7, 6, 5, 4]
        queue = PriorityQueue()
        for i in lst:
            queue.append(i)

        for i in reversed(lst):
            min_value = queue.pop()
            self.assertEqual(i, min_value)

    #@unittest.skip("demonstrating skipping")
    def test_pop(self):
        queue = PriorityQueue()
        self.assertIsNone(queue.pop())

        queue.append(10)
        self.assertEqual(10, queue.pop())
        self.assertEqual(0, len(queue))

        queue.append(10)
        queue.append(5)
        queue.append(20)

        self.assertEqual(5, queue.pop())
        self.assertEqual(2, len(queue))
        self.assertEqual(10, queue.pop())
        self.assertEqual(1, len(queue))
        self.assertEqual(20, queue.pop())
        self.assertIsNone(queue.pop())
        self.assertIsNone(queue.pop())
        self.assertEqual(0, len(queue))
