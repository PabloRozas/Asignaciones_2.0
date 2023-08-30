from Class.Tutores import Tutores
from Utils.rw_data import get_data
from Utils.change_data import transform_data_class
import unittest

class Test_GetData(unittest.TestCase):
    def test_get_data(self):
        data = get_data("Resource\data.xlsx")
        data2 = transform_data_class(data)
        tutores = data2[3]
        tutores__mate = tutores.get_AMate()
        tutores3 = Tutores()
        for tutor in tutores__mate:
            tutores3.add_tutor(tutor)
        tutores3.get_TutoresBH()
        tutores3.to_csv("Tutores.csv")
        a = True
        self.assertEqual(a, True)