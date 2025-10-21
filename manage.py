#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
Cleaned and enhanced for better readability and colorized startup logs.
"""

import os
import sys


def main():
    """Run administrative tasks with colorized output."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolwebsite.settings')

    # Optional: show clear startup info (safe for Windows)
    try:
        from colorama import Fore, Style, init
        init(autoreset=True)
        print(Fore.GREEN + "Starting Django Management Utility...")
        print(Fore.CYAN + "Using settings module:", Fore.YELLOW + os.getenv('DJANGO_SETTINGS_MODULE', 'Not set'))
        print(Style.RESET_ALL)
    except ImportError:
        # Fallback if colorama isn't installed
        print("Starting Django Management Utility...")
        print("Using settings module:", os.getenv('DJANGO_SETTINGS_MODULE', 'Not set'))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it is installed and available "
            "on your PYTHONPATH environment variable. Did you forget to "
            "activate your virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
