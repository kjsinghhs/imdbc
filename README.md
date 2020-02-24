# IMDB CLONE SUGAR BOX
Hi Welcome to the Project IMDB Clone.

Ill will guide you through how to setup an Python Environment and Configure the environment to work power up the project.

1. Install Python
        To install Python 3.X from Python.org
2. Setting up Virtual Environment
        pip install virtualenv
3. Create Folder IMDBC folder and change directory to the folder.
        3.a mkdir IMDBC
        3.b cd IMDBC
4. Now create a virtual environment
        python -m virtualenv *YourVirtualEnvName*
5. Now change directory to the virtualenv and then activate the virtual environment
        source bin/activate
6. Now install Django3.X version.
        pip install django
7. Now install Pillow (Image processing)
        pip install pillow
8. Now clone the repo from the github to the virtual environment
        8.a git clone ssh://kjsinghhs@gmail.com/kjsinghhs/imbc.git
        8.b cd src
9. Now runserver using
        python3 manage.py runserver
10. Incase the system requires to migrate use
        10.a python3 manage.py makemigrations
        10.b python3 manage.py migrate
11. Now the site is functioning. 


