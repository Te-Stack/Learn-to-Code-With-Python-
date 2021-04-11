import unittest

class TruthinessAndFalsinessTests(unittest.TestCase):
    def test_truthiness(self):
        self.assertTrue(3<5)
        self.assertTrue(1)
        self.assertTrue("hello")

    def test__falsiness(self):
        self.assertFalse(0)
        self.assertFalse(5>65)
        self.assertFalse([])
        self.assertFalse({})

if __name__ == "__main__":
    unittest.main()