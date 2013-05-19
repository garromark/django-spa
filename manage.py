#!/usr/bin/env python
import os, sys

if __name__ == '__main__':
    if os.environ["DJANGO_ENVIRON"] == "DEV":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.environments.development")
    elif os.environ["DJANGO_ENVIRON"] == "STAGING":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.environments.staging")
    elif os.environ["DJANGO_ENVIRON"] == "PROD":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.environments.production")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
