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

Below are the steps to executing the User endpoint ```http://localhost:8000/api/users/```