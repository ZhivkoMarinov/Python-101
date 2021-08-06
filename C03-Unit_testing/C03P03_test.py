import unittest
from C03P03_exception_silencing import ExceptionSilencer


class TestExceptionSilencer(unittest.TestCase):

    def test_correct_exc(self):

        with ExceptionSilencer(ValueError):
            int('aa')

        with ExceptionSilencer(IndexError):
            x = 'aa'[5]

        with ExceptionSilencer(ModuleNotFoundError):
            import mickey_mouse

    def test_wrong_exc(self):

        with self.assertRaises(ValueError):
            with ExceptionSilencer(TypeError):
                int('aa')

        with self.assertRaises(ZeroDivisionError):
            with ExceptionSilencer(SyntaxError):
                float('inf') / 0

        with self.assertRaises(ModuleNotFoundError):
            with ExceptionSilencer(EOFError):
                import mickey_mouse


if __name__ == '__main__':
    unittest.main()
