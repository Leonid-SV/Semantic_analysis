import os
# полный путь к файлу конфиг. __file__ - имя файла, в нашем случае "config.py"

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'P(*7K;lkjas9dfu'

# полный путь к базе данных
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'ToxicStackOverflow.db')

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:2409@localhost:5432/ToxicStackOverflow'


# engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')