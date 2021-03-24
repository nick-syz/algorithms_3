from KthOrderStatisticsStep import KthOrderStatisticsStep
from unittest import TestCase

class KthOrderStatisticsStepTest(TestCase):

    def test_k(self):
        arr = [3,5,2,4,1]
        self.assertEqual([4,4], KthOrderStatisticsStep(arr, 0, len(arr)-1, 4))
        
        arr = [7,5,6,4,3,1,2]
        self.assertEqual([3,3], KthOrderStatisticsStep(arr, 0, len(arr)-1, 3))

        arr = [7,6,4,5,2,3,1]
        self.assertEqual([2, len(arr)-1], KthOrderStatisticsStep(arr, 0, len(arr)-1, 3))
