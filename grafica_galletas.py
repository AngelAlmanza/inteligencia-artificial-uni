import pandas as pd
import matplotlib.pyplot as plt

#Cargar los datos desde el archivo csv
dataset = pd.read_csv("Datos_TM.csv")

x = dataset[['Diametro', 'Peso']].values
y = dataset[['Etiqueta']].values

#Separar los datos por clase
clase0 = x[y.ravel() == 0]
clase1 = x[y.ravel() == 1]
clase2 = x[y.ravel() == 2]
clase3 = x[y.ravel() == 3]


#Crear una gráfica
plt.figure(figsize=(8, 8)) #Opcional: ajusta el tamaño de la gráfica
plt.scatter(clase0[:,0], clase0[:,1], label='Canelitas', color='blue', marker='o')
plt.scatter(clase1[:,0], clase1[:,1], label='Canelitas', color='yellow', marker='o')
plt.scatter(clase2[:,0], clase2[:,1], label='Canelitas', color='red', marker='o')
plt.scatter(clase3[:,0], clase3[:,1], label='Canelitas', color='green', marker='o')
plt.xlabel('Diametro')
plt.ylabel('Peso')
plt.title('Gráfica de datos de galletas')
plt.legend()
plt.grid(True)

plt.show()