up-build:
	docker compose build
	docker compose run backend python manage.py makemigrations
	docker compose run backend python manage.py migrate
	docker compose up

build:
	docker compose build

up:
	docker compose up

migrate:
	docker compose exec backend python manage.py migrate

migrations:
	docker compose exec backend python manage.py makemigrations
	make migrate

bash:
	docker compose exec backend bash

shell:
	docker compose exec backend python ./manage.py shell

superuser:
	docker compose exec backend python ./manage.py createsuperuser

format:
	docker compose exec backend black /backend
	docker compose exec backend isort /backend
