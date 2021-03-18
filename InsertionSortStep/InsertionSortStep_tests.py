from InsertionSortStep import InsertionSortStep
from unittest import TestCase

class InsertionSortStepTest(TestCase):
    
    def test_insertion(self):
        a = [7,6,5,4,3,2,1]
        InsertionSortStep(a, 3, 0)
        self.assertEqual([1,6,5,4,3,2,7], a)
        
        InsertionSortStep(a, 2, 0)
        self.assertEqual([1,6,3,4,5,2,7], a)
        InsertionSortStep(a, 1, 0)
        self.assertEqual([1,2,3,4,5,6,7], a)

        c = [1,6,5,4,3,2,7]
        InsertionSortStep(c, 3, 1)
        self.assertEqual([1,3,5,4,6,2,7], c)
