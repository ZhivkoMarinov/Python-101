from solution import Interval
import unittest


class TestInterval(unittest.TestCase):

    def test_is_inside_closed_interval_produces_correct_result(self):
        interval = Interval(1, 10, start_opened=False, end_opened=False)

        self.assertFalse(interval.is_inside(0))
        self.assertTrue(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertTrue(interval.is_inside(10))
        self.assertFalse(interval.is_inside(15))

    def test_is_inside_opened_interval_produces_correct_result(self):
        interval = Interval(1, 10, start_opened=True, end_opened=True)

        self.assertFalse(interval.is_inside(0))
        self.assertFalse(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertFalse(interval.is_inside(10))
        self.assertFalse(interval.is_inside(15))

    def test_is_inside_start_opened_interval_produces_correct_result(self):
        interval = Interval(1, 10, start_opened=True, end_opened=False)

        self.assertFalse(interval.is_inside(0))
        self.assertFalse(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertTrue(interval.is_inside(10))
        self.assertFalse(interval.is_inside(15))

    def test_is_inside_end_opened_interval_produces_correct_result(self):
        interval = Interval(1, 10, start_opened=False, end_opened=True)

        self.assertFalse(interval.is_inside(0))
        self.assertTrue(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertFalse(interval.is_inside(10))
        self.assertFalse(interval.is_inside(15))
        
    def test_stringify_closed_interval_produces_correct_result(self):
        interval = Interval(1, 10, start_opened=False, end_opened=False)
        expected = '[1, 10]'

        self.assertEqual(expected, interval.stringify())

    def test_stringify_opened_interval_produces_correct_result(self):
        interval = Interval(1, 10, start_opened=True, end_opened=True)
        expected = '(1, 10)'

        self.assertEqual(expected, interval.stringify())

    def test_stringify_start_opened_interval_produces_correct_result(self):
        interval = Interval(1, 10, start_opened=True, end_opened=False)
        expected = '(1, 10]'

        self.assertEqual(expected, interval.stringify())

    def test_stringify_end_opened_interval_produces_correct_result(self):
        interval = Interval(1, 10, start_opened=False, end_opened=True)
        expected = '[1, 10)'

        self.assertEqual(expected, interval.stringify())


if __name__ == '__main__':
    unittest.main()
