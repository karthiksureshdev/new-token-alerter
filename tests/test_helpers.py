import unittest
from .context import helpers


class TestHelperMethods(unittest.TestCase):
    def test_parse_time(self):
        self.assertEqual(helpers.parse_time("23h 3m"), 1383)
        self.assertEqual(helpers.parse_time("3m"), 3)
        self.assertEqual(helpers.parse_time("2h"), 120)
        with self.assertRaises(ValueError):
            helpers.parse_time("1")

    def test_parse_volume(self):
        self.assertEqual(helpers.parse_money("$1.0K"), 1000)
        self.assertEqual(helpers.parse_money("$1.1M"), 1100000)
        self.assertEqual(helpers.parse_money("$1M"), 1000000)
        self.assertEqual(helpers.parse_money("1M"), 1000000)
        self.assertEqual(helpers.parse_money("1"), 1)
        with self.assertRaises(ValueError):
            helpers.parse_time("M")



if __name__ == '__main__':
    unittest.main()
