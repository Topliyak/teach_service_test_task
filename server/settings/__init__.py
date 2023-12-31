from os import environ


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = environ.get('DEBUG', 'TRUE') == 'TRUE'

if DEBUG:
    from .dev import *
