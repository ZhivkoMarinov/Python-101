import unittest
from C03P04_Fractions import Fraction


class TestFraction(unittest.TestCase):

    def test_zero_denominator(self):

        with self.assertRaises(ValueError):
            Fraction(5, 0)

    def test_is_equal(self):

        self.assertFalse(Fraction(1, 2) == Fraction(2, 3))
        self.assertTrue(Fraction(3, 5) == Fraction(3, 5))
        self.assertFalse(Fraction(1, 2) == Fraction(2, 4))

    def test_comparison(self):
        self.assertTrue(Fraction(1, 2) > Fraction(1, 3))
        self.assertTrue(Fraction(1, 5) < Fraction(1, 4))

    def test_add(self):
        test = Fraction(5, 7) + Fraction(3, 5)
        test2 = Fraction(2, 5) + Fraction(1, 5)

        self.assertTrue(Fraction(46, 35) == test)
        self.assertTrue(Fraction(3, 5) == test2)

    def test_sub(self):
        test = Fraction(5, 7) - Fraction(3, 5)
        test2 = Fraction(2, 5) - Fraction(1, 5)

        self.assertTrue(Fraction(4, 35) == test)
        self.assertTrue(Fraction(1, 5) == test2)

    def test_mul(self):
        test = Fraction(5, 9) * Fraction(3, 7)

        self.assertTrue(Fraction(15, 63) == test)

    def test_simplify(self):

        self.assertTrue(Fraction(6, 21).simplify() == Fraction(2, 7))

    def test_is_simplified(self):

        self.assertTrue(Fraction(2, 7).is_simplified())
        self.assertFalse(Fraction(6, 21).is_simplified())

    def test_list_sort(self):

        self.assertTrue(sorted([Fraction(3, 4), Fraction(1, 2)]) == [Fraction(1, 2), Fraction(3, 4)])

    def test_instance_errors(self):

        with self.assertRaises(TypeError):
            Fraction(1, 2) + 120

        with self.assertRaises(TypeError):
            Fraction(1, 2) - 20

        with self.assertRaises(TypeError):
            Fraction(1, 2) * 20


if __name__ == '__main__':
    unittest.main()
