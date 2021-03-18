from InsertionSortStep import InsertionSortStep
from unittest import TestCase

class InsertionSortStepTest(TestCase):
    
    def test_insertion(self):
        a = [1,6,5,4,3,2,7]
        InsertionSortStep(a, 3, 1)
        self.assertEqual([1,3,5,4,6,2,7], a)

        b = [1,6,5,4,3,2,7,0]
        InsertionSortStep(b, 2, 1)
        
        self.assertEqual([1,0,5,6,3,4,7,2], b)
