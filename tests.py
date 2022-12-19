import unittest

from main import progression

class TestMyApp(unittest.TestCase):
    def test_progression(self):
        n = 3
        self.assertEqual(progression(n), 11.0)

        n, start, d = 3, 5, 3
        self.assertEqual(progression(n, start, d), 11.0)

        n, start, d = 5, 5, 5
        self.assertEqual(progression(n, start, d), 25.0)

        n = -3
        with self.assertRaises(ValueError):
            progression(n, start, d)

        n = "2"
        with self.assertRaises(TypeError):
            progression(n, start, d)