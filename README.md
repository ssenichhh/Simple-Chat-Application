# Simple Chat Project

This is a Django-based web application that includes user authentication (login, signup, logout) and threaded messaging with API integration using Django REST Framework (DRF). The system allows users to communicate in message threads and includes full API coverage for message and thread management.

## Features

- User authentication (signup, login, logout)
- CRUD operations on chat threads and messages
- Thread-based messaging between two participants
- Pagination for threads and messages
- API endpoints for chat-related actions
- Unit and API tests with `pytest`
- Database integration with Django's ORM

## Requirements

To get started, ensure you have the following requirements installed:

- Python 3.8+
- Django 5.0+
- Django REST Framework (DRF)
- Pytest for testing

Install all Python dependencies:

```bash
pip install -r requirements.txt
```
## Installation

Clone this repository:

```bash

git clone https://github.com/your-username/simple-chat-project.git

```

Navigate to the project directory:

```bash

cd simple-chat-project

```

Install the dependencies:
```bash

  cd simple-chat-project
  pip install -r requirements.txt
```

Apply the migrations to set up the database:
```bash
   python manage.py migrate
   python manage.py loaddata db_test_data.json
```

Access the Django admin:
```bash
    #Superuser
    username: admin
    password: jihsu4-jambok-nUcnyp
    
    #Testuser
    username: test-user
    password: tokgAx-ninpyb-1dijhu
```

## API Endpoints

The project includes a RESTful API built with Django REST Framework (DRF). Below are some of the main endpoints:
# Threads
```bash
    GET /api/threads/ — List all threads for the authenticated user
    POST /api/threads/ — Create a new thread (only two participants allowed)
    DELETE /api/threads/<id>/ — Delete a thread (if user is a participant)

```
# Messages

```bash
    GET /api/messages/?thread_id=<id> — List messages for a specific thread
    POST /api/messages/ — Create a new message in a thread
    GET /api/messages/<id>/mark_as_read/ — Mark a message as read
    GET /api/messages/unread/ — Get unread message count

```

# Authentication
```bash
Login: Accessible at /login/, where users can log in using their username and password.
Signup: Accessible at /signup/, where users can create an account.
Logout: Accessible via /logout/.

```
# Running Tests

Unit and API tests are included for the authentication system and the messaging functionality.

To run all the tests, use pytest:
```bash
pytest
```
Test Structure
- API Tests: Located in API_tests/api_test.py, which covers CRUD operations for threads and messages.
- Auth Tests: Located in Authentication_tests/auth_test.py, which tests user login, logout, and registration.
- Models Tests: Located in Models_tests/models_test.py, which covers model testing  
# Database Models

The application includes two main models: Thread and Message.

Thread: A conversation between two users (participants).
Fields: participants, created, updated
Message: A message sent in a thread.
Fields: sender, text, thread, created, is_read