import unittest
from priority_queue_2 import PriorityQueue


class TestPriorityQueye(unittest.TestCase):
    def test_append(self):
        queue = PriorityQueue()
        queue.append(1)
        self.assertEqual(1, len(queue))

        queue.append(1)
        self.assertEqual(2, len(queue))

        queue.append(2)
        self.assertEqual(3, len(queue))

    def test_min(self):
        queue = PriorityQueue()

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

    def test_pop(self):
        queue = PriorityQueue()
        self.assertIsNone(queue.pop())

        queue.append(10)
        self.assertEqual(10, queue.pop())

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
