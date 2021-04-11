import unittest 

class InclusionTests(unittest.TestCase):
    def test_inclusion(self):
        self.assertIn("k","king")
        self.assertIn(1,[1,2,3])
        self.assertIn("a",{"a":1,"b":2})

    def test_non_inclusion(self):
        self.assertNotIn("w","king")
        self.assertNotIn("c",{"a":1,"b":2})


if __name__ == "__main__":
    unittest.main()