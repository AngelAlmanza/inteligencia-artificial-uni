from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Carga el conjunto de datos Iris
iris = load_iris()
X = iris.data
Y = iris.target

# Divide el conjunto de datos en conjuntos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Crea un modelo de red neuronal con una capa oculta de 5 neuronas
modelo = MLPClassifier(hidden_layer_sizes=5, max_iter=1000, random_state=42)

# Entrena el modelo
modelo.fit(x_train, y_train)

# Realiza predicciones en el conjunto de prueba
predicciones = modelo.predict(x_test)

# Calcula la presicion del modelo
presicion = accuracy_score(y_test, predicciones)
print(f'Presicion: {presicion}')