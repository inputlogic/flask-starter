Flask Starter
=============
This is meant to be a quick jumping point for starting new Flask projects. You
should be able to fork the repo, make a few changes and be ready for deployment
to Heroku within a few minutes.


Specifics
---------
- Python 3.6.x
- Flask 0.12
- MongoDB 3.x


Extensions Used
---------------
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [Flask-MongoEngine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
- [Flask-DebugToolbar](https://flask-debugtoolbar.readthedocs.io/en/latest/) **(Dev only)**
- [Flask-Testing](https://pythonhosted.org/Flask-Testing/) **(Dev only)**


Quickstart
----------
Ensure you have MongoDB installed. On Mac, thats super easy with Homebrew:

```
brew install mongodb
```

Then create your environment and run the project:

```
$ virtualenv -p `which python3` env
$ . env/bin/activate
$(env) make setup
$(env) make run
```


Models
------
Models are created using [MongoEngine](http://mongoengine.org) and are put into
their own module in the `app/models/` directory.

The models to be loaded at runtime must be specified in the `MODELS` config.
By default, this is located in the `config/common.py` file. The name must match
the module file and will be loaded in the order specified.

Example:

```python
MODELS = ('user', 'post', 'comment')
```


Blueprints
----------
Flask "views" in the form of Blueprints are loaded at runtime. To learn more
about Blueprints, you can [read the official Flask docs](http://flask.pocoo.org/docs/0.12/blueprints/).

Each Blueprint should exist in its own file and have the variable `bp` available
as the Blueprint instance.

The Blueprints are loaded automatically based on the `BLUEPRINTS` config found
in the `config/common.py` module.

Example config:

```python
BLUEPRINTS = ('main', 'user', 'admin')
```

Example Blueprint

```python
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
  return render_template('index.html')
```


Extensions
----------
Extensions are also loaded at runtime and can be any module with a `setup`
function. This is often used to configure other Flask extensions or custom tools
that need the app instance.

The extensions are loaded automatically based on the `EXTENSIONS` config found
in the `config/common.py` module.


Linting & Tests
---------------
Linting and tests are highly encouraged. To run them, use:

```
make quality
```

You can also run tests without linting with:

```
make test
```

And lint without testing using:

```
make lint
```


Structure
---------
- `app/` Flask project root
- `app/forms/` Form definitions for WTForm
- `app/extensions/` Modules for automatically setting up extensions at run time
- `app/models/` MongoEngine models
- `app/static/` Static assets such as CSS, JS etc.
- `app/templates/` Jinja HTML templates
- `app/views/` Flask Blueprints (routes)
- `app/__init__.py` Flask app entry point
- `config/` All configs here
- `config/common.py` Configs to be used across all environments
- `config/local.py` Configs specific to local development
- `config/production.py` Configs specific to production
- `config/test.py` Configs specific to testing
