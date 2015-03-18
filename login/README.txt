README
Mark Tamer 6411572
Rana Khalil 
To get app running: 
1. Make sure Python is installed on PC
2. Install package manager "pip" by running the following command "python get-pip.py" (On windows may be different)
3. Install a virtual environment in the same folder as where you have the app. Run the command "pip install virtualenv"
4. Create virtual environment folder run the command “virtualenv venv”
3. After installing and creating the folder the virtual environment (place where we will download all are packages and run the server) run this command 
". venv/bin/activate" this command will activate the virtual environment.
4. Once the virtual environment has been activated navigate to the the requirements.txt and run the command "pip install -r requirements.txt". This will allow us to install all dependencies and packages within the app.
5. Once that is done run these commands in the virtual command prompt you have open: 
	-> export APP_SETTINGS="lab01.config.DevConfig"
	-> export APP_MAIL_USERNAME="Your email"  (enter your email)
	-> export APP_MAIL_PASSWORD="pwd" (enter email your password)
	-> python manage.py create_db  
	-> python manage.py db init
	-> python manage.py db migrate
	-> python manage.py runserver 
6. Enjoy 
