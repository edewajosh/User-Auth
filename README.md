## User Authentication Backend ##
User-Auth is user authentication backend built using Django Rest Framework and djangorestframework-simplejwt.
Please refer to the documentation to learn more about the libraries. The project also overrides django default user authentication to add more features.

### Steps to to follow in order to run the project ###

1. Recommended that you create a virtualenv using your virtualenv library of choice e.g. venv, virtualenv, pipenv e.t.c. 
2. Navigate to your virtualenv ``` cd virtual-en ``` and activate your environment.
3. Clone the project to the created virtual environment
```git clone https://github.com/edewajosh/User-Auth.git```
4. Navigate to your project and run ```pip install -r requirements.txt ``` to install project libraries

5. You can launch the project locally by running ```python manage.py runserver ```

### How to test the authentication endpoint ###
The application has a single endpoint to enable perform POST, PUT, GET, PATCH, DELETE for User model. Since the application uses drf-simple-jwt there are three(3) other endpoints for obtaining, verifying, and refreshing token.

To list all the existing endpoints click ```http://localhost:8000/api/```.

Below are the requests to executing the User endpoint ```http://localhost:8000/api/users/```

**simple-jwt Token**

1. POST: Obtaining token : 
```127.0.0.1:8000/api/token/```
```
{
    "email": "jane.doe@example.com",
    "password": "password@123"
} 
```
2. POST: Verify token :
3. POST: Refresh token : ```127.0.0.1:8000/api/token/```
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMDQzNzgyOSwianRpIjoiNjZjZTM3NThhMDQ3NDcxMzlhOTUxMGU0ODVhNGNlOTkiLCJ1c2VyX2lkIjo0fQ.pziGk0yeY2CMCF71-jkOzcJJQQ2NB5ScDb5J8Av0Tpk"
} 
```

**User endpoint**
1. POST (Authentication Token)
*payload*
```
{
    "first_name": "Kyle",
    "last_name": "Smith",
    "email": "kyle.smith@example.com",
    "password": "password@123",
    "confirm_password": "password@123"
}
```
2. GET (Authentication Token)
*Response*
```
[
    {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@example.com",
        "is_admin": true,
        "is_active": true,
        "is_staff": true
    },
    {
        "first_name": "John",
        "last_name": "Smith",
        "email": "John.Smith@example.com",
        "is_admin": true,
        "is_active": true,
        "is_staff": true
    },
    {
        "first_name": "Lucas",
        "last_name": "Estrada",
        "email": "lucas.estrada@example.com",
        "is_admin": false,
        "is_active": false,
        "is_staff": false
    },
    {
        "first_name": "Alex",
        "last_name": "Alexander",
        "email": "alex.alexander@example.com",
        "is_admin": false,
        "is_active": false,
        "is_staff": false
    },
    {
        "first_name": "Allan",
        "last_name": "Walker",
        "email": "Alan.Walker12@example.com",
        "is_admin": false,
        "is_active": false,
        "is_staff": false
    },
    {
        "first_name": "alex12",
        "last_name": "alexander",
        "email": "alex12.alexander@example.com",
        "is_admin": false,
        "is_active": false,
        "is_staff": false
    }
]
```
3. PUT
*payload*
```
{
    "first_name": "Kyle",
    "last_name": "Smith",
    "email": "kyle.smith@example.com",
    "password": "password@123",
    "confirm_password": "password@123"
}
```
4. PATCH
5. DELETE