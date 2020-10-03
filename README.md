# Problema:

- Desconocimiento en ocasiones de la taxonomía (especie) de un árbol por parte de los técnicos. Subjetividad al asignar una especie.

- **Problema de Machine Learning:** Clasificación de nuevos árboles que se ingresen al censo árboreo.

# Dataset:

![](https://raw.githubusercontent.com/orejuelajd/tree_species_classification/master/resources/readme/dataset.PNG)

Link portal datos abiertos Santiago de Cali: http://datos.cali.gov.co/dataset/censo-arboreo-de-santiago-de-cali

# Data Pre-Processing:

- Pregunta a Expertos: Limitación del dataset por vitalidad y edad.

- Limpieza de datos: Eliminación de columnas innecearias, espacios en blanco, nombres o datos mal escritos.

- Escalamiento de datos, códificación One-Hot y Reducción de dimensionalidad PCA.

# Pipeline:

![](https://raw.githubusercontent.com/orejuelajd/tree_species_classification/master/resources/readme/pipeline.PNG)

# Importación de base de datos:

Usar el archivo .sql:

```
$ project_path/resources/database.sql
```

# Instalación En Heroku de Webservice y App:

- Activar el ambiente de desarrollo:

```
$ project_path/venv/bin/activate
```

Instalar las librerias a usar: flask para hacer build de la app y gunicorn como servidor:

```
$ pip install flask
$ pip install gunicorn
```

Heroku

El archivo requirements.txt contiene todas la librerias que instalará Heroku. Para generar el 
archivo requirements.txtfile con los módulos que se ha instalado en el ambiente/proyecto:

```
$ pip freeze > requirements.txt
```

Crear el archivo Procfile para establecer el comando que se correrá en heroku al subirse el repositorio.
Dentro del archivo Procfile escribir esto:

```
web: gunicorn app:app
```

Para subir el repositorio se deben ejecutar comandos de Git a la rama heroku master.
Git

```
$ git init .
git add --all
$ git commit -m "first commit"
$ heroku login
$ heroku git:remote -a {your-project-name}
$ git push heroku master
```