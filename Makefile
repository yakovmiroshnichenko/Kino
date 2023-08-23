run:
	python manage.py runserver
migrate:
	python manage.py migrate
migration:
	python manage.py makemigrations
clearmigrate:
	python manage.py migrate testapp zero