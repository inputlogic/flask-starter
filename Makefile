export FLASK_DEBUG=1
export FLASK_ENV=local
export FLASK_APP=app/__init__.py

clean:
	find app -iname '*.pyc' -exec rm {} \;
	find config -iname '*.pyc' -exec rm {} \;

migrate:
	flask db migrate

upgrade:
	flask db upgrade

downgrade:
	flask db downgrade

setup:
	pip install -r requirements.txt
	pip install -r requirements.local.txt
	$(MAKE) migrate
	$(MAKE) upgrade

run: clean
	flask run
