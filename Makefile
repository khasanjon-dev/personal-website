del:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

make:
	python3 manage.py makemigrations

mig:
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser --username admin