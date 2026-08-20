import sys
import os

# Obtener la ruta del directorio padre (soporte/)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Agregar el directorio padre al sys.path
sys.path.insert(0, parent_dir)

from settings.settings import GLPI_USER, GLPI_PASSWORD, GLPI_DATABASE, GLPI_HOST;
import mysql.connector as cn ;

connector_db = cn.connect(
    host=GLPI_HOST,
    user=GLPI_USER,
    password=GLPI_PASSWORD,
    database=GLPI_DATABASE
)

