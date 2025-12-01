import sys
import os

# Ruta del proyecto
project_path = os.path.dirname(os.path.abspath(__file__))
if project_path not in sys.path:
    sys.path.append(project_path)

# Importar Flask app
from app import app as application
