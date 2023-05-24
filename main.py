import pandas as pd

from Resource.change_data import transform_data_class
from Resource.rw_data import get_data



# Se leen los datos
data = get_data("Resource\data.xlsx")

# Se transforman los datos a objetos de las clases correspondientes
alumnos_vae, alumnos_pace, alumnos_solicitudes, tutoresC = transform_data_class(data)

alumnos_vae.print_alumnos()
alumnos_pace.print_alumnos()
alumnos_solicitudes.print_alumnos()
tutoresC.print_tutores()