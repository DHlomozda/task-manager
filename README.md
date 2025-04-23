# Task manager project

## Project about task manager. 
This is a pet project about task manager. Here you can add task, worker with position and task types.
Use login: admin password: 123

## Installation
Python 3.12 must be already installed

```shell
https://task-manager-0nd6.onrender.com/
git clone https://github.com/DHlomozda/task-manager.git
cd task_manager_project
pyhton -m venv .venv
venv\Scripts\Activate
pip install -r requirements.txt
python manage.py populate_data # to fill data base with fake data
python manage.py createsuperuser # to create user for login
python manage.py runserver # starts Django server
```

## Features
* Sign up functionality for Worker
* Managing task

## Demo
![Website Interface](demo.png)
