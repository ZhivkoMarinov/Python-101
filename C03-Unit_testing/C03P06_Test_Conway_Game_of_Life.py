import unittest
from unittest.mock import patch
from solution import ConwayGame


class TestConwayGame(unittest.TestCase):

    def test_structure(self):
        app = ConwayGame(100, 100, [12, 314, 2278, 8419])

        with self.subTest('if structure() method calls construct_gif() method'):
            with patch('solution.ConwayGame.construct_gif') as method:
                app.structure()
                method.assert_called()

        with self.subTest('if structure() method calls calculate_next_image() method properly'):
            with patch('solution.ConwayGame.calculate_next_image') as method:
                app.structure()
                self.assertGreater(method.call_count, 1)

    def test_calculate_next_image(self):
        app = ConwayGame(100, 100, [1, 2, 3])

        with self.subTest('3 live in row'):
            self.assertEqual(app.calculate_next_image({1112: 1, 1113: 1, 1114: 1, 1013: 0, 1213: 0}),
                             {1112: 0, 1113: 1, 1114: 0, 1013: 1, 1213: 1})

            self.assertEqual(app.calculate_next_image({1712: 1, 1713: 1, 1715: 1}),
                             {1712: 0, 1713: 0, 1715: 0})

        with self.subTest('3 live in column'):
            self.assertEqual(app.calculate_next_image({2375: 1, 2474: 0, 2475: 1, 2476: 0, 2575: 1}),
                             {2375: 0, 2474: 1, 2475: 1, 2476: 1, 2575: 0})

            self.assertEqual(app.calculate_next_image({2275: 1, 2475: 1, 2575: 1}),
                             {2275: 0, 2475: 0, 2575: 0})

        with self.subTest('3 live in L or ˩ combination'):
            self.assertEqual(app.calculate_next_image({2275: 1, 2276: 0, 2375: 1, 2376: 1}),
                             {2275: 1, 2276: 1, 2375: 1, 2376: 1})

            self.assertEqual(app.calculate_next_image({2175: 1, 2176: 1, 2275: 0, 2276: 1}),
                             {2175: 1, 2176: 1, 2275: 1, 2276: 1})

        with self.subTest('3 live in left or right diagonal'):
            self.assertEqual(app.calculate_next_image({2275: 1, 2376: 1, 2477: 1}),
                             {2275: 0, 2376: 1, 2477: 0})

    def test_construct_gif(self):
        app = ConwayGame(100, 100, [12, 312, 4447, 6667, 9531])

        with self.subTest('If is called with valid args'):
            with patch('solution.ConwayGame.construct_gif') as method:
                app.run_app()
                self.assertEqual(type(method.call_args[0][0][0]), dict)

    def test_is_key_existing(self):
        app = ConwayGame(100, 100, [12, 312, 4447, 6667, 9531])
        cells_map = {0: 1, 32: 1, 4145: 1}

        with self.subTest('if key exists'):

            self.assertTrue(app.is_key_existing(cells_map, 32))
            self.assertTrue(app.is_key_existing(cells_map, 4145))

            self.assertFalse(app.is_key_existing(cells_map, 31))
            self.assertFalse(app.is_key_existing(cells_map, 412))


if __name__ == '__main__':
    unittest.main()

