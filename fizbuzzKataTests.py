import unittest
from fizbuzzKata import transform


class TestSum(unittest.TestCase):
    def test_transform_returnsArrayValueWithEmptyList(self):
        fizzbuzzList = []
        result = transform(fizzbuzzList)
        self.assertEqual(result,[])
    def testListWIht1_transform_returnsListWithValue1(self):
        fizzbuzzList = [1]
        result = transform(fizzbuzzList)
        self.assertEqual(result,[1])
    def testListWIht1and2_transform_returnsListWithValue1and2(self):
        fizzbuzzList = [1,2]
        result = transform(fizzbuzzList)
        self.assertEqual(result,[1,2])
        

if __name__ == '__main__':
    unittest.main()