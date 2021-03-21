from QuickSortTailOptimization import QuickSortTailOptimization
from unittest import TestCase
import random

class QuickSortTailOptimizationTest(TestCase):

    def test_quick(self):
        arr = [1,3,4,6,11,5,9,8,2,7]
        check = sorted(arr[:])
        QuickSortTailOptimization(arr, 0, len(arr)-1)

        self.assertEqual(check, arr)

        random_lst = [i for i in range(100)]
        random.shuffle(random_lst)
        check = random_lst[:]
        QuickSortTailOptimization(random_lst, 0, len(random_lst)-1)
        self.assertEqual(sorted(check), random_lst)
