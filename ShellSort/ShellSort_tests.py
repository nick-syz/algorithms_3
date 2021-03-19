from ShellSort import InsertionSortStep, KnuthSequence
from unittest import TestCase

class ShellSortTest(TestCase):

    def test_shell(self):
        arr = []
        for j in range(41, 0, -1):
            arr.append(j)
        check_arr = arr[:]
        seq = KnuthSequence(len(arr))
        for i in seq:
            InsertionSortStep(arr, i, 0)
        
        print(check_arr)
        self.assertEqual(seq, [40,13,4,1])
        self.assertEqual(arr, sorted(check_arr))
