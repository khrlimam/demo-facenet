## Few things on this template:
1. `loader.py`: This file has one function: `load(app)` this function will loads all apps blueprint.
2. `boot.py`: this file contains applications boots. Here Flask application will be started
3. `config.py`: Here we define all Flask required configurations (e.g DB URI, and so on) and our own configurations
4. `server.py`: This file will serve the app requests.
5. `views` directory: here we define all apps blueprints. Each blueprint need to be registered on `loader.py` so the blueprint will works
6. `seeds` directory: Take a look at it, you will understand. This directory is optional
7. `models` directory: Here we define our model and table structure. Each models need to be imported in `manage.py` file so the flask-migration can recognize each model and their structures then migrate them.
8. `manage.py`: This file is cli into database migrations and seeder. Below is how to use it

## Built in commands
1. manage.py
  - **Init migrations**: `python manage.py db init`
  - **Migrate models into table schema**: `python manage.py db migrate`
  - **Build table schema into real table**: `python manage.py db upgrade`
  - **Init table records**: `python manage.py seed`
2. flask
  - **Run the app**: `flask run`. Make sure you exported `FLASK_APP` variable which defines the file location that contains `flask.run()` method, in our case that is `server.py`. So the exported command would be look like `export FLASK_APP=$(pwd)/server.py`