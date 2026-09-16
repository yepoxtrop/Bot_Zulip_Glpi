from enum import Enum;
from textwrap import dedent

class Rustdesk_Messages(Enum):
    
    MESSAGE_RUSDESK_OS = dedent("""
        💻 ¿Qué sistema operativo utilizas? Así te enviaré el archivo correcto para obtener tu **ID de RustDesk**:

        - `1` → Linux
        - `2` → Windows 10 u 11
    """)
    
    MESSAGE_RUSDESK_URL_FILE = dedent("""
        ✅ Descarga el archivo desde este enlace:

        [URL_ARCHIVO]

        📋 Cuando lo ejecutes, se mostrará tu **ID de RustDesk**.
        El equipo de soporte podrá solicitarte ese ID para conectarse.
    """)