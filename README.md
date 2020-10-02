And let's activate it with the source command:
´´´
$ source venv/bin/activate
´´´

Then, let's use pip to install the libraries we're going to use - flask to build the app and gunicorn as our server:

$ pip install flask
$ pip install gunicorn

Heroku

To achieve this, we need to create a requirements.txt file with all of the modules:

$ pip freeze > requirements.txt

For Heroku to be able to run our application like it should, we need to define a set of processes/commands that it should run beforehand. These commands are located in the Procfile:

web: gunicorn app:app

Git

To upload our code, we'll use Git. First, let's make a git repository:

$ git init .
git add --all
$ git commit -m "first commit"

Alternatively, we can login using the browser if we run the command:

$ heroku login

At this point, while logged in, we should add our repository to the remote one:

$ heroku git:remote -a {your-project-name}

And with that done, let's upload the project by pushing it to Heroku:

$ git push heroku master

Test

https://{your-project-name}.herokuapp.com/