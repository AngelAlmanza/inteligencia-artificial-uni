import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Agregar los datos
# x Son las caracteristicas
# y Son las clases del etiquetado

x = np.array([
  [1, 2],
  [2, 3],
  [1, 3],
  [2, 2],
  [3, 4],
  [3, 2],
  [4, 2],
  [3, 3]
])

y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Dividir los datos en un conjunto de entrenamiento y prueba
x_train, x_text, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Crear clasificador KNN
k = 5 # Numero de vecinos cercanos a considerar
knn_classfier = KNeighborsClassifier(n_neighbors=k)

# Entrenar el clasificador KNN  con los datos de entrenamiento
knn_classfier.fit(x_train, y_train)

# Clasificamos un nuevo dato
dato_nuevo = [[2, 1]]
prediccion = knn_classfier.predict(dato_nuevo)
print(f'El nuevo dato pertenece a la clase {prediccion}')

# Separar los puntos por clase
clase_0 = x[y == 0]
clase_1 = x[y == 1]

# Crear un nuevo grafico
plt.figure(figsize=(8, 6))

# Graficar los puntos de la clase 0 en amarillo
plt.scatter(clase_0[:, 0], clase_0[:, 1], c='yellow', label='Clase 0')

# Graficar los puntos de la clase 1 en azul
plt.scatter(clase_1[:, 0], clase_1[:, 1], c='blue', label='Clase 1')

# Graficar el nuevo dato
plt.scatter(2, 1, c='red', label='Nuevo dato')

# Agregar etiquetas de los ejes
plt.xlabel('Diametro')
plt.ylabel('Area')
plt.legend()

# Mostrar el grafico
plt.grid(True)
plt.savefig('grafico.png')


# EJERCICIO

x = np.array([
  [10, 0],
  [0, -10],
  [5, -2],
  [5, 10],
  [0, 5],
  [5, 5]
])

y = np.array([0, 0, 0, 1, 1, 1])

x_train, x_text, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

k = 3
knn_classfier = KNeighborsClassifier(n_neighbors=k)
knn_classfier.fit(x_train, y_train)

dato_nuevo = [[2, 1]]
prediccion = knn_classfier.predict(dato_nuevo)
print(f'El nuevo dato pertenece a la clase {prediccion}')

clase_0 = x[y == 0]
clase_1 = x[y == 1]

plt.figure(figsize=(8, 6))
plt.scatter(clase_0[:, 0], clase_0[:, 1], c='yellow', label='Clase 0')
plt.scatter(clase_1[:, 0], clase_1[:, 1], c='blue', label='Clase 1')
plt.scatter(2, 1, c='red', label='Nuevo dato')
plt.xlabel('Diametro')
plt.ylabel('Area')
plt.legend()
plt.grid(True)
plt.savefig('grafico_tarea.png')
