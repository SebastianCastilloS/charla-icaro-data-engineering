# Hands-on: Desplegando un modelo de Machine Learning

Repositorio creado para alojar el código requerido para el hands-on de la charla de Data Engineering para #LaSemanaDeLosDatos organizada por [Icaro](https://icaro.org.ar/).

## Pre-requisitos

Tener instalado [Python 3.X](https://www.python.org/downloads/windows/) en la computadora donde se haga el ejercicio.

Es sugerido el uso de un ambiente virtualizado para evitar corromper la instalación local de Python. [Acá](https://help.dreamhost.com/hc/es/articles/115000695551-Instalar-y-usar-virtualenv-con-Python-3) hay una muy buena guía para instalar la librería `virtualenv`.

## Objetivo del ejercicio
Con este ejercicio se busca tener un primer acercamiento a lo que sería disponibilizar un modelo de Machine Learning pre-armado para su uso.

Vamos a correr un script que generará un modelo predictivo y lo guardará en un archivo para luego ser usado por una página web para devolver predicciones.

## Uso

Bajen una copia del código alojado en este repositorio (pueden forkear el repositorio o bajarlo como un zip) y sigan los siguientes pasos adentro de la carpeta bajada.


0) Opcional para virtualizar: ejecutar el siguiente comando para crear un ambiente virtual de Python
```Bash
python3 -m venv icaro
```
2) Instalación de dependencias. En este paso instalaremos las librerias requeridas para ejecutar el script.

```bash
# Con el ambiente virtual
source icaro/bin/activate 
pip install -r requirement.txt
```
```bash
# Sin el ambiente virtual
python3 -m pip install -r requirement.txt
```
3) Correr script de generación de modelo
```bash
# Con el ambiente virtual
python model.py
```
```bash
# Sin el ambiente virtual
python3 model.py
```
4) Correr script que levanta web server con página, el cual genera el output con el link al localhost.
```bash
# Con el ambiente virtual
python app.py
```
```bash
# Sin el ambiente virtual
python3 app.py
```
```bash
# Output del comando
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 292-919-338
```
5) Ingresar al link mencionado, [http://127.0.0.1:5000/](http://127.0.0.1:5000/), e interactuar con la aplicación =)
6) Volver a la terminal y apretar `CTRL y C`.

## Conclusiones

En este taller revisamos una manera de generar un modelo y serializarlo en un archivo para posteriormente ser usado en una API y simple página web.

Esto es una pequeña representación de lo que se suele llamar cómo modelos predictivos online, y es usado por muchas aplicaciones para tener respuestas en tiempo real, tales cómo scoring crediticios en bancos, sugerencias de productos en páginas de marketplace, validaciones de identidad y más.

