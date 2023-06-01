import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join('.env')
load_dotenv(dotenv_path)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
print(SECRET_KEY)