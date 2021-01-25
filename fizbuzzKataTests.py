import unittest

def transform(number):
        return number

class TestSum(unittest.TestCase):
    def test_transform_returnsArrayValueWith1(self):
        array = [1]
        result = transform(array)
        self.assertEqual(result, [1])

if __name__ == '__main__':
    unittest.main()