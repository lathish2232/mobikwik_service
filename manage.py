#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobikwik.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)



from jproperties import Properties
def read_properties():
    file_path = "resources/app-config_dev.properties"
    configs = Properties()
    with open(file_path, 'rb') as config_file:
        configs.load(config_file)
        host = configs.get("DB_HOST").data
        is_auth = configs.get("is_AUTH").data
        database = configs.get("db").data
    os.environ['DB_HOST'] = host
    os.environ['is_AUTH'] = is_auth
    os.environ['db'] = database


if __name__ == '__main__':
    read_properties()
    main()
