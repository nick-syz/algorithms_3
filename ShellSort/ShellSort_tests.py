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
        
        self.assertEqual(seq, [40,13,4,1])
        self.assertEqual(arr, sorted(check_arr))
        
        self.assertEqual(1, len(KnuthSequence(1)))
        
        seq2 = KnuthSequence(13)
        self.assertEqual([13,4,1], seq2)

        seq3 = KnuthSequence(0)
        self.assertEqual([1], seq3)
