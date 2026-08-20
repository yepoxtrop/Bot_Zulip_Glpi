# VARIABLES DE ENTORNO PARA LA BASE DE DATOS GLPI
import os;
from dotenv import load_dotenv;

load_dotenv();
GLPI_USER=os.getenv("GLPI_USER");
GLPI_PASSWORD=os.getenv("GLPI_PASSWORD")
GLPI_DATABASE=os.getenv("GLPI_DATABASE")
GLPI_HOST=os.getenv("GLPI_HOST")
