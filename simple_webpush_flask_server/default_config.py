SERVER_NAME = 'localhost:5000'

DB_USERNAME = 'master'
DB_PASSWORD = 'm@sterP@ssw0rd'
DB_SERVER = 'localhost'
DB_NAME = 'simple_webpush_demo'

SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{user}:{passwd}@{server}/{db}".format(user=DB_USERNAME, passwd=DB_PASSWORD, server=DB_SERVER, db=DB_NAME)