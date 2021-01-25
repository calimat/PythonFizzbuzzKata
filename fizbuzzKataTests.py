import unittest

def transform(number):
    return number

class TestSum(unittest.TestCase):
    def test_transform_returnsArrayValueWith1(self):
        array = [1]
        result = transform(array)
        self.assertEqual(result, [1])
    def test_transform_returnsArrayValueWith1And2(self):
        array = [1,2]
        result = transform(array)
        self.assertEqual(result, [1,2])
    def test_transform_returnsArrayValueWith1And2AndFizz(self):
        array = [1,2, 3]
        result = transform(array)
        self.assertEqual(result, [1,2, "Fizz"])

if __name__ == '__main__':
    unittest.main()