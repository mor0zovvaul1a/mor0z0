import unittest
from src.greeter import Greeter

class TestGreeter(unittest.TestCase):
    def test_greet(self):
        g = Greeter("alice")
        self.assertEqual(g.greet(), "Hello, Alice!")

if __name__ == "__main__":
    unittest.main()
