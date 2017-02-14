import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'd1c27e62636803a422aa6fc9617fdd24e428d7e961f00491'
UPLOAD_FOLDER = basedir+'/cms/static/upload/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'])

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'myapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
