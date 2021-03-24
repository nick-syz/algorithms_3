from MergeSort import MergeSort
from unittest import TestCase
import random

class MergeSortTest(TestCase):

    def test_merge(self):
        arr = [5,4,2,1,6]
        self.assertEqual([1,2,4,5,6], MergeSort(arr))

        arr = [2,1]
        self.assertEqual([1,2], MergeSort(arr))

        arr = [1]
        self.assertEqual([1], MergeSort(arr))

        arr = []
        self.assertEqual([], MergeSort(arr))

        arr = [i for i in range(100)]
        check = arr[:]
        random.shuffle(arr)
        self.assertEqual(sorted(check), MergeSort(arr))
