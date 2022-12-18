import unittest

from main import progression

class TestMyApp(unittest.TestCase):
    def test_progression(self):
        start, d, n = 2, 3, 3
        self.assertEqual(progression(start, d, n), 15.0)

        start, d, n = 2, -3, 3
        self.assertEqual(progression(start, d, n), -3.0)

        start, d, n = 0, 0, 0
        self.assertEqual(progression(start, d, n), 0.0)

        start, d, n = 2, 3, -3
        with self.assertRaises(ValueError):
            progression(start, d, n)

        start, d, n = "2", 3, 2
        with self.assertRaises(TypeError):
            progression(start, d, n)