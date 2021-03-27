from BinarySearch import BinarySearch
from unittest import TestCase

class BinarySearchTest(TestCase):
    
    def test_search(self):
        a = [1,2,3,4,5,6,7]
        search = BinarySearch(a)
        search.Step(2)
        self.assertEqual(0, search.GetResult())
        self.assertEqual(0, search.Left)
        self.assertEqual(2, search.Right)

    def test_search1(self):
        a = [1,2,3,4,5,6,7]
        search = BinarySearch(a)
        search.Step(4)
        self.assertEqual(1, search.GetResult())
        self.assertEqual(0, search.Left)
        self.assertEqual(6, search.Right)

    def test_search3(self):
        a = [1,2]
        search = BinarySearch(a)
        search.Step(3)
        self.assertEqual(-1, search.GetResult())
        self.assertEqual(2, search.Left)
        self.assertEqual(1, search.Right)

    def test_search4(self):
        a = [1,2,3,4,5,6,7]
        search = BinarySearch(a)
        search.Step(7)
        while search.GetResult() == 0:
            search.Step(7)
        self.assertEqual(1, search.GetResult())
        self.assertEqual(6, search.Left)
        self.assertEqual(6, search.Right)

    def test_search5(self):
        a = [1,2,4,6,7]
        search = BinarySearch(a)
        
        search.Step(3)
        self.assertEqual(0, search.GetResult())
        self.assertEqual(0, search.Left)
        self.assertEqual(1, search.Right)
        
        search.Step(3)
        self.assertEqual(-1, search.GetResult())
        self.assertEqual(2, search.Left)
        self.assertEqual(1, search.Right)
