import unittest
from generator.name_generator import generate_name

class TestNameGen(unittest.TestCase):
    def test_generate_name(self):
        result = generate_name()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
