from KthOrderStatisticsStep import KthOrderStatisticsStep
from unittest import TestCase
import random

class KthOrderStatisticsStepTest(TestCase):

    def test_k(self):
        arr = [3,5,2,4,1]
        self.assertEqual([0,4], KthOrderStatisticsStep(arr, 0, len(arr)-1, 4))

        arr = [8,3,16,2,18,13,11,4,14,17,1,10,6,12,9,20,7,19,15,5]
        self.assertEqual([5,5], KthOrderStatisticsStep(arr, 0, len(arr)-1, 5))
