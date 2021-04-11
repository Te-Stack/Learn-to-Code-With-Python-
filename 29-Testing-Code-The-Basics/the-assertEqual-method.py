import unittest

class TestStringMethod(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a","b","c"])
        self.assertEqual("d+e+f".split("+"), ["d","e","f"])

    def test_count(self):
        self.assertEqual("beautiful".count("u"),2)

    def test_length(self):
        self.assertEqual(len("help"),4)




if __name__ == "__main__":
    unittest.main()