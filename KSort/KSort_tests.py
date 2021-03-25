from KSort import ksort
from unittest import TestCase

class KSortTest(TestCase):
    
    def test_add(self):
        arr = ['a01', 'b64', 'g99', 'b46', 'a10', 'b00']
        k_sort = ksort()
        for i in arr:
            self.assertTrue(k_sort.add(i))
        res = []
        for i in k_sort.items:
            if i is not None:
                res.append(i)
        arr = sorted(arr)
        self.assertEqual(arr, res)

        self.assertIsNone(k_sort.items[k_sort.index('b01')])
        
    def test_check(self):
        k_sort = ksort()
        self.assertFalse(k_sort.add('y12'))
        self.assertFalse(k_sort.add('12'))
        self.assertFalse(k_sort.add('y123'))
    
    def test_index(self):
        k_sort = ksort()
        self.assertEqual(164, k_sort.index('b64'))
        self.assertEqual(11, k_sort.index('a11'))
        self.assertEqual(101, k_sort.index('b01'))
        self.assertEqual(110, k_sort.index('b10'))
