from HeapSort import HeapSort
from unittest import TestCase

class HeapSortTest(TestCase):

    def test_heap(self):
        a = [9,2,4,1,5,7,8]
        heap = HeapSort(a)
        self.assertEqual(7,heap.HeapObject.count)

        b = []
        out = heap.GetNextMax()
        while out != -1:
            b.append(out)
            out = heap.GetNextMax()

        self.assertEqual([9,8,7,5,4,2,1], b)
