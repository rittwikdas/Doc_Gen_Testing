import unittest
from generator import generate_document

class TestDocGeneration(unittest.TestCase):
    def test_non_empty_output(self):
        doc = generate_document()
        self.assertTrue(len(doc) > 100)

    def test_section_presence(self):
        doc = generate_document()
        self.assertIn("Project Overview", doc)
        self.assertIn("Pipeline Details", doc)

if __name__ == "__main__":
    unittest.main()
