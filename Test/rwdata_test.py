from Utils.rw_data import get_data
import unittest

class Test_GetData(unittest.TestCase):
    def test_get_data(self):
        data = get_data("Resource\data.xlsx")
        self.assertEqual(len(data), 4)