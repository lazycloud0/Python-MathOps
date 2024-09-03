# test_math_operators

import unittest
from math_ops import addition, subtraction, multiplication, division, modulus, exponentiation, floor_division

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(5, 3), 8, "Addition failed: 5 + 3 should equal 8")
        self.assertEqual(addition(-1, 1), 0, "Addition failed: -1 + 1 should equal 0")
        self.assertEqual(addition(0, 0), 0, "Addition failed: 0 + 0 should equal 0")

class TestSubtraction(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(subtraction(10, 4), 6, "Subtraction failed: 10 - 4 should equal 6")
        self.assertEqual(subtraction(5, 10), -5, "Subtraction failed: 5 - 10 should equal -5")
        self.assertEqual(subtraction(0, 0), 0, "Subtraction failed: 0 - 0 should equal 0")

class TestMultiplication(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(multiplication(6, 7), 42, "Multiplication failed: 6 * 7 should equal 42")
        self.assertEqual(multiplication(8, 0), 0, "Multiplication failed: 8 * 0 should equal 0")
        self.assertEqual(multiplication(-3, 4), -12, "Multiplication failed: -3 * 4 should equal -12")

class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(15, 3), 5, "Division failed: 15 / 3 should equal 5")
        self.assertAlmostEqual(division(10, 3), 3.3333333333333335, places=7, msg="Division failed: 10 / 3 should approximately equal 3.3333333")
        self.assertEqual(division(5, 0), "Error: Division by zero", "Division failed: 5 / 0 should return an error message")

class TestModulus(unittest.TestCase):
    def test_modulus(self):
        self.assertEqual(modulus(17, 5), 2, "Modulus failed: 17 % 5 should equal 2")
        self.assertEqual(modulus(25, 7), 4, "Modulus failed: 25 % 7 should equal 4")
        self.assertEqual(modulus(10, 0), "Error: Modulus by zero", "Modulus failed: 10 % 0 should return an error message")

class TestExponentiation(unittest.TestCase):
    def test_exponentiation(self):
        self.assertEqual(exponentiation(2, 3), 8, "Exponentiation failed: 2 ** 3 should equal 8")
        self.assertEqual(exponentiation(5, 0), 1, "Exponentiation failed: 5 ** 0 should equal 1")
        self.assertEqual(exponentiation(0, 5), 0, "Exponentiation failed: 0 ** 5 should equal 0")

class TestFloorDivision(unittest.TestCase):
    def test_floor_division(self):
        self.assertEqual(floor_division(17, 5), 3, "Floor division failed: 17 // 5 should equal 3")
        self.assertEqual(floor_division(-17, 5), -4, "Floor division failed: -17 // 5 should equal -4")
        self.assertEqual(floor_division(5, 0), "Error: Division by zero"),