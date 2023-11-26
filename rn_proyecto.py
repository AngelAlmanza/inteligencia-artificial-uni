from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Cargar el conjunto de datos Breast Cancer Wisconsin
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos (importante para las redes neuronales)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear un modelo de red neuronal para clasificación con una capa oculta de 5 neuronas
modelo = MLPClassifier(hidden_layer_sizes=5, max_iter=1000, random_state=42)

# Entrenar el modelo
modelo.fit(X_train_scaled, y_train)

# Realizar predicciones en el conjunto de prueba
predicciones = modelo.predict(X_test_scaled)

# Calcular la precisión del modelo
precision = accuracy_score(y_test, predicciones)
print(f'Precisión del modelo en el conjunto de prueba: {precision}')
