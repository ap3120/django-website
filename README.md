# Django-Website
A very minimal website I built while learning Django.

# Install dependencies
This website requires a few python packages. To install packages from the requirements.txt file in a Django project, follow these steps:
- Open the command prompt or terminal and navigate to the root directory of your Django project.
- Activate your virtual environment using the command source path/to/venv/bin/activate (replace "path/to/venv" with the actual path to your virtual environment).
- Run the command pip install -r requirements.txt to install all the packages listed in the requirements.txt file.

Note: Make sure that the requirements.txt file is present in the root directory of your Django project, and it contains all the necessary packages along with their versions.

After installing the packages, you can verify whether the packages are installed correctly or not by running the command pip freeze in the terminal. This will display a list of all the installed packages along with their versions.

# Run The Website
To run the website navigate to upper level "mysite" directory and run the command via cmd: *python3 manage.py makemigrations* then *python3 manage.py migrate* and then *python3 manage.py runserver*.
Then you should see a local host link that you can copy into your browser to see the website.

# Test suite
To run the tests navigate the the upper "mysite" directory and run via cmd: *python3 manage.py test*.
