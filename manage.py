#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from os.path import join, dirname
from dotenv import load_dotenv


def load_into_config():
    import os

    from CabPriceCoefficientApp.apps import CabPriceCoefficientAppConfig

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    CabPriceCoefficientAppConfig.REDIS_HOST = os.environ.get("REDIS_HOST")
    CabPriceCoefficientAppConfig.REDIS_PORT = os.environ.get("REDIS_POST")
    CabPriceCoefficientAppConfig.MYSQL_HOST = os.environ.get("MYSQL_HOST")
    CabPriceCoefficientAppConfig.MYSQL_PORT = os.environ.get("MYSQL_PORT")
    CabPriceCoefficientAppConfig.MYSQL_USER = os.environ.get("MYSQL_PORT")
    CabPriceCoefficientAppConfig.MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")



def main():
    """Run administrative tasks."""
    load_into_config()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CabPriceCoefficientProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
