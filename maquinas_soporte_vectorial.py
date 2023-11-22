import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd

# Cargar los datos del CSV
dataset = pd.read_csv("./Datos_TM.csv")

# Supongamos que tenemos una columna "x" y una columna "y" en el archivo CSV
X = dataset[['Diametro', 'Peso']].values
Y = dataset['Etiqueta'].values

# Dividimos los datos en conjuntos de entrenamientos y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Creamos el clasificador SVM
svm_classifier = SVC(kernel='linear') # Usamos un kernel lineal

# Entrenamos el modelo SVM
svm_classifier.fit(X_train, Y_train)

# Realizamos las predicciones en el conjunto de prueba
predictions = svm_classifier.predict(X_test)

# Calculamos la presicion del modelo
accuracy = accuracy_score(Y_test, predictions)
print(f"Presicion del modelo SVM: {accuracy}")
print("El numero de datos de pruebas es de %d" % X_test.shape[0])

# Separar los datos por clases
clase0 = X[Y == 0]
clase1 = X[Y == 1]
clase2 = X[Y == 2]
clase3 = X[Y == 3]

# Crear una grafica de dispersion (scatter plot)
plt.figure(figsize=(8, 8)) # Opcional - Ajusta el tamaño de la grafica
plt.scatter(clase0[:, 0], clase0[:, 1], label="Canelitas", color="blue", marker="o")
plt.scatter(clase1[:, 0], clase1[:, 1], label="Marias", color="yellow", marker="o")
plt.scatter(clase2[:, 0], clase2[:, 1], label="Crackes", color="red", marker="o")
plt.scatter(clase3[:, 0], clase3[:, 1], label="Coco", color="green", marker="o")
plt.xlabel('Diametro')
plt.ylabel('Peso')
plt.title('Grafica de datos de galletas')
plt.legend()

# Mostrar el grafico
plt.grid(True)
plt.show()