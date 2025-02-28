import unittest
from image_sanitizer.detector import ImageSanitizer

class TestImageSanitizer(unittest.TestCase):
    def setUp(self):
        self.sanitizer = ImageSanitizer(model_path="models/model.h5")

    def test_classification(self):
        result = self.sanitizer.classify("tests/sample_safe.jpg")
        self.assertIn(result, ["NSFW", "Safe"])

if __name__ == "__main__":
    unittest.main()
