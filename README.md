# Secure-Authentication

# Usage

Creating a secure authentication for a school. The app should allow users to reset there passwords and be try to be as secure as possible.

## About

## To Install

To get app running: 
  1. Make sure Python is installed on PC
  2. Install package manager "pip" by running the following command "python get-pip.py" (On windows may be different)
  3. Install a virtual environment in the same folder as where you have the app. Run the command "pip install virtualenv"
  4. Create virtual environment folder run the command “virtualenv venv”
  3. After installing and creating the folder the virtual environment (place where we will download all are packages and run the server) run this command 
". venv/bin/activate" this command will activate the virtual environment.
  4. Once the virtual environment has been activated navigate to the the requirements.txt and run the command "pip install -r requirements.txt". This will allow us to install all dependencies and packages within the app.
  5. Once that is done run these commands in the virtual command prompt you have open: 
  ``` python
      1.-> export APP_SETTINGS="lab01.config.DevConfig" 
      
      2.-> export APP_MAIL_USERNAME="Your email"  (enter your email)
      
      3.-> export APP_MAIL_PASSWORD="pwd" (enter email your password)
      
      4.-> python manage.py create_db
      
      5.-> python manage.py db init
      
      6.-> python manage.py db migrate
      
      7.-> python manage.py runserver 
      
      6. Enjoy!
  ```

##Notes
I added an upload page, make sure the upload path is relative to your workstation. 
