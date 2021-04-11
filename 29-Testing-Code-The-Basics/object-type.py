import unittest

class ObjectTypeTests(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1,int)
        self.assertIsInstance(5.2,float)


    def test_not_is_instance(self):
        self.assertNotIsInstance(1,float)
        self.assertNotIsInstance(2.1,dict)


if __name__ == "__main__":
    unittest.main()