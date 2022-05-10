import environ
from project.settings import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRETE_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db('DATABASE_URL'),
}
