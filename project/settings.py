import os
from dotenv import load_dotenv
from environs import Env

load_dotenv()

env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=False)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS'), '127.0.0.1']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True