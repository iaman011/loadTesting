import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()


'''
write this command:
>> coverage run -m unittest test_calculator.py
>> coverage report

to get the coverage report:
reporting html doc:
>> coverage html
>> start htmlcov/index.html
'''