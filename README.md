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
