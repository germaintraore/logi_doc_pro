#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Sous Windows, enregistrement automatique du chemin des DLLs PostgreSQL pour psycopg2
if sys.platform == "win32":
    for pg_ver in ["18", "17", "16", "15"]:
        pg_bin = rf"C:\Program Files\PostgreSQL\{pg_ver}\bin"
        if os.path.exists(pg_bin):
            try:
                os.add_dll_directory(pg_bin)
            except Exception:
                pass
            break


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
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
