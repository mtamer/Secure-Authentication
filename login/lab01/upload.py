import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from lab01 import app

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


