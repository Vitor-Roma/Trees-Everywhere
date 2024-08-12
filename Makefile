start:
	docker compose down
	docker compose up --build

run:
	docker compose down
	docker compose up

up:
	docker compose down
	docker compose up -d

down:
	docker compose down

migrations:
	docker exec -it trees_everywhere python manage.py makemigrations

build:
	docker exec -it trees_everywhere python manage.py migrate

admin:
	docker exec -it trees_everywhere python manage.py createsuperuser --username admin

load_data:
	docker exec -it trees_everywhere python manage.py loaddata */fixtures/*.json

test:
	docker exec -it trees_everywhere python manage.py test