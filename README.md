# News Board
Python 3, Django and Django REST Framework (for REST API)
## Overview
Basic models:<br />
- `Post`
- `Comment`

Functional Requirements:<br />
- `CRUD API` to manage news posts:
    - `/api/posts/` view all posts (GET, POST request method)
    - `/api/posts/<post_id>/` (PUT, DELETE request methods)

- `CRUD API` to manage comments:
    
-  endpoint to upvote the post:
    - `/api/posts/<post_id>/upvote/`
    
Technical Requirements:<br />
- `Flake8` linter