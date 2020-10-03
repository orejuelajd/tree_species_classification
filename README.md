Problema:

Dataset:

Problema de Machine Learning:

Data Pre-Processing:

Pregunta a Expertos:
Limpieza de datos:
Escalamiento de datos y Reducción de dimensionalidad:

Resultados:

Conclusiones:

Arquitectura:

Importación de base de datos:

Instalación En Heroku de Webservice y App:

- Activar el ambiente de desarrollo:

´´´
$ project_path/venv/bin/activate
´´´

Instalar las librerias a usar: flask para hacer build de la app y gunicorn como servidor:

´´´
$ pip install flask
$ pip install gunicorn
´´´

Heroku

El archivo requirements.txt contiene todas la librerias que instalará Heroku. Para generar el 
archivo requirements.txtfile con los módulos que se ha instalado en el ambiente/proyecto:

´´´
$ pip freeze > requirements.txt
´´´

Crear el archivo Procfile para establecer el comando que se correrá en heroku al subirse el repositorio.
Dentro del archivo Procfile escribir esto:

´´´
web: gunicorn app:app
´´´

Para subir el repositorio se deben ejecutar comandos de Git a la rama heroku master.
Git

´´´
$ git init .
git add --all
$ git commit -m "first commit"
$ heroku login
$ heroku git:remote -a {your-project-name}
$ git push heroku master
´´´