# Automobile Management System 

API to manage automobile inventory, including vehicle listings, dealership information, sales transactions, and maintenance records. This system will enable users to manage vehicles, handle sales, and track maintenance, providing a robust solution for automobile management.


## Prerequisites
- Python 3.x
- Django
- djangorestframework
- djangorestframework-simplejwt

## Installation

1. **Clone the repository**

    ```bash
    git https://github.com/Micode360/Automobile-Management-System-API.git
    cd Automobile_Management_System_API
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    ```bash
    pip install django djangorestframework djangorestframework-simplejwt

    ```

4. **Run migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser to access the admin site**

    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server**

    ```bash
    python manage.py runserver
    ```

Open your browser and visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to log in to the admin site and manage memos. 
