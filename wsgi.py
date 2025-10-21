"""
WSGI config for schoolwebsite project.

This file exposes the WSGI callable as a module-level variable named `application`.
It is used by WSGI-compatible web servers (e.g., Gunicorn, uWSGI) to serve your Django app.

For more information, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Optional: colored startup message (safe for Windows console)
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    print(Fore.GREEN + "Django WSGI application initialized using:", 
          Fore.CYAN + os.getenv('DJANGO_SETTINGS_MODULE', 'Not set'),
          Style.RESET_ALL)
except ImportError:
    # Fallback if colorama isn't installed
    print("Django WSGI application initialized using:", os.getenv('DJANGO_SETTINGS_MODULE', 'Not set'))

# ✅ Set default settings module for the 'schoolwebsite' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolwebsite.settings')

application = get_wsgi_application()
