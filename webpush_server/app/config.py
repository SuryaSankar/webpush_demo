SERVER_NAME = 'localhost:5000'

#Database
DB_USERNAME = 'master'
DB_PASSWORD = 'm@sterP@ssw0rd'
DB_SERVER = 'localhost'
DB_NAME = 'webpush_demo'

SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{user}:{passwd}@{server}/{db}".format(user=DB_USERNAME, passwd=DB_PASSWORD, server=DB_SERVER, db=DB_NAME)

SECRET_KEY = 'SomeString'
SECURITY_REGISTERABLE = True
SECURITY_PASSWORD_SALT = 'SomePasswordSalt'
SECURITY_SEND_REGISTER_EMAIL = False
APPLICATION_SERVER_PUBLIC_KEY = "BGV0Zro6QSeKDjPXqnW-nscEIEbNNS_qYTFDCxEw6bJuzfbHxpxbUiKkSun_iLbE_yROwJlcmPugILgs3MTejKI"