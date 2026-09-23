import os
import sys

# Sous Windows, enregistrement automatique du répertoire des DLLs PostgreSQL
if sys.platform == "win32":
    for pg_ver in ["18", "17", "16", "15"]:
        pg_bin = rf"C:\Program Files\PostgreSQL\{pg_ver}\bin"
        if os.path.exists(pg_bin):
            try:
                os.add_dll_directory(pg_bin)
            except Exception:
                pass
            break
