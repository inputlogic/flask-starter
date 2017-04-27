Flask Starter
=============

This is meant to be a quick jumping point for starting new Flask projects. You should be able to
fork the repo, make a few changes and be ready for deployment to Heroku within a few minutes.


Quickstart
----------

```
$ virtualenv -p `which python3` env
$ . env/bin/activate
$(env) pip install -r requirements.txt
$(env) pip install -r requirements.local.txt
$(env) . setup.sh
$(env) flask db migrate
$(env) flask db upgrade
$(env) flask run
```
