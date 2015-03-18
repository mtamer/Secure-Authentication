import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""

    # main config
    SECRET_KEY = '\x05\x05\xf6"\x1fn\xecG\xa7,l\\e}\xe8\xfb:\xa25\xc0\x8b\xac\xf5$'
    SECURITY_PASSWORD_SALT = '\\\x80\xe5\xc6\x82\x18\x0b\xc1\x0c\xb7\xf3|\xecY\x0c\xe5/!\x84Gif\x88?'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    SECURITY_EMAIL_SENDER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

    # mail accounts
    MAIL_DEFAULT_SENDER = 'vice-chair@ieeeuttawa.ca'\

    #upload
    # ALLOWED_EXTENSIONS  = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    # UPLOAD_FOLDER = '/Users/Mark/Desktop/CSI4139/Assignmnents/lab1/Lab01_6411572_RanaStudentnumber/login/lab01/uploads'

class DevConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    DEBUG_TB_ENABLED = True
