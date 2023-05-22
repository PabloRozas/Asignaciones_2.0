import pandas as pd

from Resource.change_data import transform_data_class
from Resource.rw_data import get_data



# Se leen los datos
data = get_data("Resource\data.xlsx")

print(data[0].head())
print(data[1].head())
print(data[2].head())
print(data[3].head())


# fila 347 de data[2]
# print(data[2].iloc[347])

# transform_data_class(data)
