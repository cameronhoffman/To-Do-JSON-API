run:
	FLASK_APP=main.py FLASK_DEBUG=1 flask run

seed:
	PYTHONPATH=.:$$PYTHONPATH python db/seeds.py

test:
	PYTHONPATH=.:$$PYTHONPATH pytest --disable-pytest-warnings
