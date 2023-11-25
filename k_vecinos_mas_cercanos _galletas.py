import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Agregar los datos
# x Son las caracteristicas
# y Son las clases del etiquetado

# Cargar los datos del CSV
dataset = pd.read_csv('./Datos_TM.csv')

X = dataset[['Diametro', 'Peso']].values
Y = dataset['Etiqueta'].values

# Dividir los datos en un conjunto de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Crear clasificador KNN
k = 5 # Numero de vecinos cercanos a considerar
knn_classfier = KNeighborsClassifier(n_neighbors=k)

# Entrenar el clasificador KNN  con los datos de entrenamiento
knn_classfier.fit(x_train, y_train)


# Clasificar con los datos de pruebas
prediccion = knn_classfier.predict(x_test)

# Clasificar la presicion de la clasificacion
accuracy = accuracy_score(y_test, prediccion)
print(f'Presicion: {accuracy * 100:.2f}%')
print("El numero de datos de pruebas es de %d" % x_test.shape[0])

# Separar los puntos por clase
clase_0 = X[Y == 0]
clase_1 = X[Y == 1]
clase_2 = X[Y == 2]
clase_3 = X[Y == 3]

# Crear un nuevo grafico
plt.figure(figsize=(8, 6))

plt.scatter(clase_0[:, 0], clase_0[:, 1], c='yellow', label='Canelitas', marker='o')
plt.scatter(clase_1[:, 0], clase_1[:, 1], c='blue', label='Marias', marker='o')
plt.scatter(clase_2[:, 0], clase_2[:, 1], c='red', label='Cracker', marker='o')
plt.scatter(clase_3[:, 0], clase_3[:, 1], c='green', label='Coco', marker='o')

# Graficar el nuevo dato
plt.scatter(2, 1, c='red', label='Nuevo dato')

# Agregar etiquetas de los ejes
plt.xlabel('Diametro')
plt.ylabel('Area')
plt.title('Grafica Galletas')
plt.legend()

# Mostrar el grafico
plt.grid(True)
plt.savefig('grafico_k_vecinos_mas_cercanos.png')


# EJERCICIO

# x = np.array([
#   [10, 0],
#   [0, -10],
#   [5, -2],
#   [5, 10],
#   [0, 5],
#   [5, 5]
# ])

# y = np.array([0, 0, 0, 1, 1, 1])

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# k = 3
# knn_classfier = KNeighborsClassifier(n_neighbors=k)
# knn_classfier.fit(x_train, y_train)

# dato_nuevo = [[2, 1]]
# prediccion = knn_classfier.predict(dato_nuevo)
# print(f'El nuevo dato pertenece a la clase {prediccion}')

# clase_0 = x[y == 0]
# clase_1 = x[y == 1]

# plt.figure(figsize=(8, 6))
# plt.scatter(clase_0[:, 0], clase_0[:, 1], c='yellow', label='Clase 0')
# plt.scatter(clase_1[:, 0], clase_1[:, 1], c='blue', label='Clase 1')
# plt.scatter(2, 1, c='red', label='Nuevo dato')
# plt.xlabel('Diametro')
# plt.ylabel('Area')
# plt.legend()
# plt.grid(True)
# plt.savefig('grafico_tarea.png')
