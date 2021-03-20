from ArrayChunk import ArrayChunk
from unittest import TestCase

class ArrayChunkTest(TestCase):

    def test_chunk(self):
        M =  [7,5,6,4,3,1,2]
        self.assertEqual(3, ArrayChunk(M))
        self.assertEqual([2,1,3,4,6,5,7], M)

        M = [1,2,3,8,5,6,7]
        self.assertEqual(6, ArrayChunk(M))
        self.assertEqual([1,2,3,7,5,6,8], M)

        M = [1,2,3,8,5,9,10]
        self.assertEqual(3, ArrayChunk(M))
        self.assertEqual([1,2,3,5,8,9,10], M)

        M = [1,2,3,10,9,8]
        self.assertEqual(5, ArrayChunk(M))
        self.assertEqual([1,2,3,8,9,10], M)

        M = [1,3,4,6,5,2,8]
        self.assertEqual(5, ArrayChunk(M))
        self.assertEqual([1,3,4,2,5,6,8], M)

        M = [1,3,2]
        self.assertEqual(1, ArrayChunk(M))
        self.assertEqual([1,2,3], M)

        M = [2,1]
        self.assertEqual(1, ArrayChunk(M))
        self.assertEqual([1,2], M)
