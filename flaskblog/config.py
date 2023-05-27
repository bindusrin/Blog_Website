#import os


class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    SECRET_KEY = '5a006e562642ef02fea0564e085b50f4'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
