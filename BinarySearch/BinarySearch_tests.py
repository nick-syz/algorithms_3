from BinarySearch import BinarySearch, GallopingSearch
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
        self.assertEqual(1, search.Left)
        self.assertEqual(1, search.Right)
    
    def test_search3_1(self):
        a = [1,2]
        search = BinarySearch(a)
        search.Step(0)
        self.assertEqual(-1, search.GetResult())
        self.assertEqual(0, search.Left)
        self.assertEqual(-1, search.Right)

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
        a = [1,2,4,6,7,9,10]
        search = BinarySearch(a)
        
        search.Step(3)
        self.assertEqual(0, search.GetResult())
        self.assertEqual(0, search.Left)
        self.assertEqual(2, search.Right)
        
        search.Step(3)
        self.assertEqual(-1, search.GetResult())
        self.assertEqual(2, search.Left)
        self.assertEqual(2, search.Right)
    
    def test_search6(self):
        a = [i for i in range(1, 100)]
        search = BinarySearch(a)

        search.Step(49)
        self.assertEqual(0, search.GetResult())
        self.assertEqual(0, search.Left)
        self.assertEqual(48, search.Right)

        search.Step(49)
        self.assertEqual(0, search.GetResult())
        self.assertEqual(25, search.Left)
        self.assertEqual(48, search.Right)

        search.Step(49)
        self.assertEqual(0, search.GetResult())
        self.assertEqual(37, search.Left)
        self.assertEqual(48, search.Right)

        search.Step(49)
        self.assertEqual(0, search.GetResult())
        self.assertEqual(43, search.Left)
        self.assertEqual(48, search.Right)

        search.Step(49)
        self.assertEqual(0, search.GetResult())
        self.assertEqual(46, search.Left)
        self.assertEqual(48, search.Right)

        search.Step(49)
        self.assertEqual(1, search.GetResult())
        self.assertEqual(48, search.Left)
        self.assertEqual(48, search.Right)
    
    def test_galloping(self):
        a = [i for i in range(1, 100)]

        self.assertTrue(GallopingSearch(a, 5))
        self.assertFalse(GallopingSearch(a, -1))
        self.assertFalse(GallopingSearch(a, 100))
        self.assertTrue(GallopingSearch(a, 50))
        self.assertTrue(GallopingSearch(a, 99))
        self.assertFalse(GallopingSearch(a, 1000))
        self.assertTrue(GallopingSearch(a, 50))
        self.assertFalse(GallopingSearch(a, -1000))

        self.assertFalse(GallopingSearch([], 5))
