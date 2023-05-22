from Resource.change_data import transform_data_class
from Resource.rw_data import get_data

# Se leen los datos
data = get_data("Resource\data.xlsx")

print(data[0]) # Se imprime Pace
print(data[1]) # Se imprime Solicitud
print(data[2]) # Se imprime VAE
print(data[3]) # Se imprime Tutores


# fila 347 de data[2]
# print(data[2].iloc[347])

# transform_data_class(data)
