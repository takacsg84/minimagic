import unittest

from minimagic import generate_cool_name, id_cudnn_available, is_cudnn__version_available


class TestGeneral(unittest.TestCase):
    def test_cool_name(self):
        cool_name = generate_cool_name()
        self.assertGreater(len(cool_name), 0)

    def test_cudnn_availability(self):
        self.assertIsNot(id_cudnn_available(), None)
        for v in [7, 8, 9, 10, 11]:
            self.assertIsNot(is_cudnn__version_available(version=v), None)
