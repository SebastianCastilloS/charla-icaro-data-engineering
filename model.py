# Importar las librerias necesarias
import numpy as np # Libreria para manejar arrays en Python de manera eficiente
import pandas as pd # Libreria para manejar datos de manera eficiente y simple
import pickle # Libreria para serializar representacion de objetos
import json # Libreria para manejar jsons 

# Nos traemos el CSV con la información
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Dividimos el set de datos en subsets para entrenar y probar el modelo
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Realizamos una regresión linear
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Realizamos una predicción sobre el subset de test
y_pred = regressor.predict(X_test)

# Guardaamos el modelo en la carpeta local
pickle.dump(regressor, open('model.pkl','wb'))

# Cargamos el modelo y mostramos el valor de una predicción con un input random
model = pickle.load( open('model.pkl','rb'))
print(model.predict([[1.8]]))
