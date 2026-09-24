from src.settings.settings import GLPI_USER, GLPI_PASSWORD, GLPI_DATABASE, GLPI_HOST;
import mysql.connector as cn ;

connector_db = cn.connect(
    host=GLPI_HOST,
    user=GLPI_USER,
    password=GLPI_PASSWORD,
    database=GLPI_DATABASE
)