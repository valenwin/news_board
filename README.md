# News Board
Python 3, Django and Django REST Framework (for REST API)
## Overview
Basic models:<br />
- `Post`
- `Comment`

Functional Requirements:<br />
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
    - GET `/api/comments/<comment_id>/` ex: `/api/comments/1/`
    - GET `/api/comments/<comment_id>/post` ex: `/api/comments/1/post/`
    - POST `/api/comments/`
    - PUT `/api/comments/<comment_id>/` ex: `/api/comments/1/`
    - DELETE `/api/comments/<comment_id>/` ex: `/api/comments/1/`
    
-  endpoint to upvote the post:
    - `/api/posts/<post_id>/upvote/`
    
Technical Requirements:<br />
- `Flake8` linter