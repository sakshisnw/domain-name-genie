import unittest
from generator.tagline_generator import generate_tagline

class TestTaglineGen(unittest.TestCase):
    def test_generate_tagline(self):
        result = generate_tagline()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
