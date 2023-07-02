# ChatApp using Django

This is a simple chat application built using the Django framework. It allows users to register, log in, and chat with each other in real-time.

![ChatApp Screenshot]()

## Features

- User registration: Users can create a new account by providing their email address and password.
- User authentication: Users can log in to the application using their registered email address and password.
- Real-time chat: Users can send and receive messages in real-time with other logged-in users.
- User profiles: Each user has a profile that displays their username and profile picture.
- Room management APIs: APIs are provided to create, update, and delete rooms in the app.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3
- Django
- HTML,CSS,JavaScript
- Django REST Framework


## Installation

1. Clone the repository:
   git clone <repository-url>

2. Create a virtual environment:
   python3 -m venv env

3. Activate the virtual environment:
- For Windows:
  ```
  env\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source env/bin/activate
  ```

4. Install the dependencies:
 ```
   pip install -r requirements.txt
```
   
6. Set up the database:
- If you're using PostgreSQL, create a new database and update the `DATABASES` configuration in `settings.py` with your database credentials.
- If you're using a different database, update the `DATABASES` configuration accordingly.

6. Apply the database migrations:

7. Start the development server:
   ```
   python manage.py runserver
   ```

9. Access the application in your web browser at `http://localhost:8000`.

## Configuration

- `SECRET_KEY`: The secret key used by Django. Make sure to set a strong, unique secret key in `settings.py`.
- `DEBUG`: Set this to `True` during development and `False` in production.
- `ALLOWED_HOSTS`: Add the hostnames or IP addresses that will be allowed to access the application.
- `DATABASES`: Configure the database settings according to your database setup.

## Room Management APIs

The following APIs are available for managing rooms in the app:

- `GET /api/rooms/`: Get a list of all rooms.
- `GET /api/rooms/{room_id}/`: Get details of a specific room.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request to the GitHub repository.


## Acknowledgements

- The Django project: [https://www.djangoproject.com/](https://www.djangoproject.com/)
- Django Channels: [https://channels.readthedocs.io/](https://channels.readthedocs.io/)

## Contact

If you have any questions or need further assistance, feel free to contact the project maintainer at [abhiapor543@gmail.com]




