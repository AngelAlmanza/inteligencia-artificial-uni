import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd
import seaborn as sns

#Cargar los datos desde el archivo csv
dataset = pd.read_csv("Datos_TM.csv")

x = dataset[['Diametro', 'Peso']].values
y = dataset[['Etiqueta']].values

#Dividir el conjunto de datos en entrenamiento y pruebas
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

#Crear clasificadoor Bayesino
clf = GaussianNB()

#Entrenando el clasificador con el 70% de datos
clf.fit(X_train, y_train)

#Predicciones
y_pred = clf.predict(X_test)

#Calcular la precisión de las predicciones
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del clasificador Naive Bayes: {accuracy:.2f}")
print("El numero de datos de pruebas es de %d" % X_test.shape[0])

#Separar los datos por clase
clase0 = x[y.ravel() == 0]
clase1 = x[y.ravel() == 1]
clase2 = x[y.ravel() == 2]
clase3 = x[y.ravel() == 3]

#Crear una gráfica
plt.figure(figsize=(8, 8)) #Opcional: ajusta el tamaño de la gráfica
plt.scatter(clase0[:,0], clase0[:,1], label='Canelitas', color='blue', marker='o')
plt.scatter(clase1[:,0], clase1[:,1], label='Marias', color='yellow', marker='o')
plt.scatter(clase2[:,0], clase2[:,1], label='Crackers', color='red', marker='o')
plt.scatter(clase3[:,0], clase3[:,1], label='Coco', color='green', marker='o')
plt.xlabel('Diametro')
plt.ylabel('Peso')
plt.title('Gráfica de datos de galletas')
plt.legend()

# Mostrar el grafico
plt.grid(True)
plt.show()