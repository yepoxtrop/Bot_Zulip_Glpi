# VARIABLES DE ENTORNO PARA LA BASE DE DATOS GLPI
import os;
from dotenv import load_dotenv;

load_dotenv();
GLPI_USER=os.getenv("GLPI_USER");
GLPI_PASSWORD=os.getenv("GLPI_PASSWORD");
GLPI_DATABASE=os.getenv("GLPI_DATABASE");
GLPI_HOST=os.getenv("GLPI_HOST");
ZULIP_URL=os.getenv("ZULIP_URL");
GLPI_URL=os.getenv("GLPI_URL");
NUMERO_SOPORTE1=os.getenv("NUMERO_SOPORTE1");
NUMERO_SOPORTE2=os.getenv("NUMERO_SOPORTE2");
CORREO_SOPORTE=os.getenv("CORREO_SOPORTE");