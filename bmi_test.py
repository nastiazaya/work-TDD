import unittest
from bmiF import BMI

class MyTestCase(unittest.TestCase): #Unit test
    def test_0(self):
        self.assertAlmostEqual(BMI(40, 173), 'Underweight')
    def test_1(self):
        self.assertAlmostEqual(BMI(50, 157), 'Healthy weight')
    def test_2(self):
        self.assertAlmostEqual(BMI(69, 157), 'over-weight')
    def test_3(self):
        self.assertAlmostEqual(BMI(95, 172), 'obesity')
    def test_4(self):
        self.assertAlmostEqual(BMI(120, 180), 'Severe fat')
    def test_5(self):
        self.assertAlmostEqual(BMI(162, 197), 'Severe obesity')
    def test_6(self):
        self.assertAlmostEqual(BMI(-162, 197), 'You are having trouble entering again')
    def test_7(self):
        self.assertAlmostEqual(BMI(162, -197), 'You are having trouble entering again')
    def test_8(self):
        self.assertAlmostEqual(BMI(-162, -197), 'You are having trouble entering again')

if __name__ == '__main__':
    unittest.main()
