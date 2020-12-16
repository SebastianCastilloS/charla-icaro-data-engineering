# Importar librerias requeridas
import numpy as np # numpy es una libreria para manejar vectores de una manera más óptima y sencilla
from flask import Flask, request, jsonify, render_template # flask es una libreria para generar APIs y páginas web en Python de manera sencilla
import pickle # pickle es una libreria para serializar / deserializar datos

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# Se carga el template html localizado en la carpeta /templates/index.html
@app.route('/')
def home():
    return render_template('index.html')

# Decorador y función que devuelve la predicción en la página web
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # Extraemos los valores del formulario
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    # Llamamos a la funcion con el modelo serializado pasandole cómo parámetro los valores recolectados
    prediction = model.predict(final_features)

    # Redondeamos el valor devuelto por la función
    output = round(prediction[0], 2)

    # Retornamos la predicción en la página web, reemplazando el placeholder prediction_text
    return render_template('index.html', prediction_text='El salario predecido es: {}'.format(output))

# Decorador y función que devuelve la prediccón a traves de un método POST
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    # Extraemos los valores del formulario
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    # Llamamos a la funcion con el modelo serializado pasandole cómo parámetro los valores recolectados
    prediction = model.predict(final_features)

    # Redondeamos el valor devuelto por la función
    output = round(prediction[0], 2)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
