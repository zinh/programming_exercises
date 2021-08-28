import unittest
from median_two_array import Solution

class TestMedianTwoArray(unittest.TestCase):
    @unittest.skip("skip")
    def test_median_two_array(self):
        median = Solution()
        # [1,2,3] -> 2
        self.assertEqual(2, median.findMedianSortedArrays([1,3], [2]))
        # [1,2,3,4] -> 2.5
        self.assertEqual(2.5, median.findMedianSortedArrays([1,2], [3,4]))
        self.assertEqual(0, median.findMedianSortedArrays([0, 0], [0, 0]))
        self.assertEqual(1, median.findMedianSortedArrays([], [1]))
        self.assertEqual(2, median.findMedianSortedArrays([2], []))
