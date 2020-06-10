## Neeramitra Reddy - 171CO101
## Veena Nagar - 171CO151


### Setting up MySQL

- `sudo apt-get update`
- `sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev`
- `sudo apt-get install wkhtmltopdf`
- `sudo mysql_secure_installation`
- `mysql -u root -p`
- `create database restaurant character set utf8;`
- `create user restaurantuser@localhost identified by 'Password@0';`
- `grant all privileges on restaurant.* to restaurantuser@localhost;`
- `flush privileges;`
- `exit`


### Setting up Django

- `sudo pip install virtualenv`
- `python3 -m venv myvenv`
- `source myvenv/bin/activate`
- `pip install django mysqlclient`
- `pip install pdfkit`
- `pip install django-tellme`
- `pip install Pillow`

### Running the project

- `cd ~/restaurant`
- `python manage.py makemigrations`
- `python manage.py sqlmigrate orders 0001`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`

Go to http://127.0.0.1:8080/admin/
