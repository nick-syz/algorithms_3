from QuickSort import QuickSort
from unittest import TestCase
import random

class QuickSortTest(TestCase):

    def test_quick(self):
        arr = [9,8,7,6,5,4,3,2,1]
        QuickSort(arr, 0, len(arr)-1)
        self.assertEqual([1,2,3,4,5,6,7,8,9], arr)

        arr = [1,2,3,9,8,7,6]
        QuickSort(arr, 0, len(arr)-1)
        self.assertEqual([1,2,3,6,7,8,9], arr)
        
        arr = [1,3,4,6,11,5,9,8,2,7]
        QuickSort(arr, 0, len(arr)-1)
        self.assertEqual([1,2,3,4,5,6,7,8,9,11], arr)
        
        random_lst = [i for i in range(100)]
        random.shuffle(random_lst)
        check = random_lst[:]
        QuickSort(random_lst, 0, len(random_lst)-1)
        self.assertEqual(sorted(check), random_lst)

    def test_quick1(self):
        arr = [9,8,7,6,5,4,3]
        QuickSort(arr, 3, len(arr)-1)
        self.assertEqual([9,8,7,3,4,5,6], arr)
        
        QuickSort(arr, 1, len(arr)-1)
        self.assertEqual([9,3,4,5,6,7,8], arr)

        QuickSort(arr, 0, len(arr)-1)
        self.assertEqual([3,4,5,6,7,8,9], arr)
