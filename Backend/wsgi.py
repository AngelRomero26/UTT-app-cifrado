import sys
import os

# → Ruta absoluta al directorio de tu proyecto
project_home = '/home/angelr0195/UTT-app-cifrado/Backend'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.chdir(project_home)

# Importa la app Flask como application (requisito de WSGI)
from app import app as application
