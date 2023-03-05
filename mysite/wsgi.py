"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

project_folder = os.path.expanduser('/Users/hannahgersten/Desktop/NYU/Spring 2023/SWE/Django-Tutorial/mysite/mysite/')  # noqa E501
load_dotenv(os.path.join(project_folder, '.env'))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
