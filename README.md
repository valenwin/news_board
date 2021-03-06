# News Board

## Overview
### Basic models:<br />
- `Post`
- `Comment`

### Functional Requirements:<br />
- `/api/` major link

- `CRUD API` to manage news posts:
    - GET `/api/posts/` 
    - GET `/api/posts/<post_id>/` ex: `/api/posts/1/`
    - GET `/api/posts/<post_id>/comments` ex: `/api/posts/1/comments`
    - POST `/api/posts/`
    - PUT `/api/posts/<post_id>/` ex: `/api/posts/1/`
    - DELETE `/api/posts/<post_id>/` ex: `/api/posts/1/`
    
- `CRUD API` to manage comments:
    - GET `/api/comments/` 
    - GET `/api/comments/<comment_id>/` e.g. `/api/comments/1/`
    - GET `/api/comments/<comment_id>/post` e.g. `/api/comments/1/post_details/`
    - POST `/api/comments/`
    - PUT `/api/comments/<comment_id>/` e.g. `/api/comments/1/`
    - DELETE `/api/comments/<comment_id>/` e.g. `/api/comments/1/`
    
-  endpoint to upvote the post:
    - `/api/posts/<post_id>/upvote/`

- reset post upvotes count:
    - `Celery` periodic task: reset_post_upvotes()
    
### Technical Requirements:<br />
- Python 3, Django and Django REST Framework (for REST API)
- `Postman` collection:
    - import file NewsBoard.postman_collection.json
- Docker container settings (Dockerfile, docker-compose.yml)
- Code formatted with `Black`
    - black {source_file_or_directory}
- `Flake8` linter (.travis.yml)
    - flake8 news_board
- `Heroku` deployment link:<br />
    https://news-board-api.herokuapp.com/

## Deploy project on your local machine

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Insert your own db configuration settings (see example.env):
and change file name to .env:

`SECRET_KEY`<br />

`DB_PASSWORD`<br />
`DB_NAME`<br />
`DB_USER`<br />

3 - Migrate db models to PostgreSQL:

`python3 manage.py migrate`

4 - Run app:

`python3 manage.py runserver`

5 - Run Celery:

`celery -A news_board worker -l info`<br />
launch RabbitMQ by using `rabbitmq-server` or `brew services run rabbitmq`