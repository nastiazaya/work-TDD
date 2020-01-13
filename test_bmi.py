import unittest
from bmiF import BMI

class MyTestCase(unittest.TestCase): #Unit test
    def test_something(self):
        self.assertAlmostEqual(BMI(40, 173), 'Underweight')
        self.assertAlmostEqual(BMI(50, 157), 'Healthy weight')
        self.assertAlmostEqual(BMI(69, 157), 'over-weight')
        self.assertAlmostEqual(BMI(95, 172), 'obesity')
        self.assertAlmostEqual(BMI(120, 180), 'Severe fat')
        self.assertAlmostEqual(BMI(162, 197), 'Severe obesity')
        self.assertAlmostEqual(BMI(-162, 197), 'You are having trouble entering again')
        self.assertAlmostEqual(BMI(162, -197), 'You are having trouble entering again')
        self.assertAlmostEqual(BMI(-162, -197), 'You are having trouble entering again')

if __name__ == '__main__':
    unittest.main()
