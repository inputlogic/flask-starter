export FLASK_DEBUG=1
export FLASK_ENV=local
export FLASK_APP=run.py

.PHONY: clean setup run test lint quality

clean:
	find app -iname '*.pyc' -exec rm {} \;
	find config -iname '*.pyc' -exec rm {} \;

setup:
	pip install -r requirements.txt
	pip install -r requirements.local.txt

run: clean
	flask run

test:
	FLASK_ENV=test python -W ignore -m unittest discover -s tests -p "test_*.py"

lint:
	flake8 --statistics app

quality: test lint

# Scripts
# Must be in the form of modules so we can import other areas of the app

resetdb:
	python -m scripts.resetdb

superuser:
	python -m scripts.superuser

shell:
	ptpython --interactive=scripts/shell.py
