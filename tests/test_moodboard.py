import unittest
from generator.moodboard import generate_moodboard_keywords

class TestMoodboardGen(unittest.TestCase):
    def test_generate_keywords(self):
        result = generate_moodboard_keywords("SmartCloud")
        self.assertIsInstance(result, list)
        self.assertTrue(any("smartcloud" in kw.lower() for kw in result))

if __name__ == '__main__':
    unittest.main()
