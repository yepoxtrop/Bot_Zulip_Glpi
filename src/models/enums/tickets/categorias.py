from enum import Enum;

class Categorias(Enum):
    ACS__ELIMINACION_DE_ELEMENTOS_ADVERSOS = [0, "Eliminación de elementos adversos"];
    ACS__ELIMINACION_DE_GLOSAS_DE_CONCURRENCIA = [0, "Eliminación de glosas de concurrencia"];
    ACS__ELIMINACION_DE_INOPORTUNIDADES = [0, "Eliminación de inoportunidades"];
    ACS__ELIMINACION_DE_NOTAS_DE_CONCURRENCIA = [0, "Eliminación de notas de concurrencia"];
    ACS__SOPORTE_DE_EXPORTABLE_DE_CONCILIACIONES_PENDIENTES_POR_EJECUTAR = [0, "Soporte de exportable de conciliaciones pendientes por ejecutar"];
    ACS__SOPORTE_DEL_USO_DEL_SISTEMA_ACS_MEDICAL_CONCURRENCIA = [0, "Soporte del uso del sistema ACS Medical concurrencia"];
    ACS__DISTRIBUCION_DE_CONCURRENCIA = [0, "Distribución de concurrencia"];
    SISTEMAS__APLICACIONES = [2, "Aplicaciones"];
    SISTEMAS__ARCHIVOS = [2, "Archivos"];
    SISTEMAS__CAPACITACION = [2, "Capacitación"];
    SISTEMAS__CARPETA_COMPARTIDA = [2, "Carpeta compartida"];
    SISTEMAS__E_MAIL = [2, "E-mail"];
    SISTEMAS__IMPRESORAS = [2, "Impresoras"];
    SISTEMAS__PERIFERICOS = [2, "Periféricos"];
    SISTEMAS__VPN = [2, "VPN"];
    SISTEMAS__CREACION_DE_USUARIO = [2, "Creacion de Usuario"];
    SISTEMAS__SOLUCIONES_MAYOR_A_HORAS = [2, "Solución mayor a 5 horas"];
    SISTEMAS__CONEXION_A_ESCRITORIO_REMOTO = [2, "Conexion a Escritorio Remoto"];
    SISTEMAS__DAÑO_DE_EQUIPO_DE_COMPUTO = [2, "Daño de Equipo de Computo"];
    SISTEMAS__RED_INTERNET = [2, "Red-Internet"];
    SISTEMAS__SOLICITUD_DE_EQUIPO_DE_COMPUTO = [2, "Solicitud de Equipo de Computo"];
    SISTEMAS__CORRECTIVOS = [2, "Correctivos"];
    SISTEMAS__SOLICITUD_DE_CAMBIO = [2, "Solicitud de Cambio"];
    SISTEMAS__CORRECTIVO_CON_TRASLADO = [2, "Correctivo con Traslado"];
    FOMAG__APLICAIONES = [3, "Aplicaciones"];
    FOMAG__CONEXION_A_ESCRITORIO_REMOTO = [3, "Conexion a Escritorio Remoto"];
    FOMAG__DAÑO_DE_EQUIPO_DE_COMPUTO = [3, "Daño de Equipo de Computo"];
    FOMAG__SOLUCIONES_MAYOR_A_HORAS = [3, "Solución mayor a 5 horas"];
    FOMAG__VPN = [3, "VPN"];
    AUDITORIA_MEDICA__SOPORTE_ACS = [4, "Soporte ACS"];
    AUDITORIA_MEDICA__SOPORTE_AUDITORIA = [4, "Soporte Auditoria"];
    
# STRCUTURE
#   [id_entities, name_categorie]