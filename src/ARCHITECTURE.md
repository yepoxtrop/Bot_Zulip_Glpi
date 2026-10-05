# Estructura Hexagonal

Esta estructura agrega capas nuevas sin mover ni modificar los modulos actuales.

```text
src/
src/
├── domain/                  Capa Central: Reglas y lógica pura de negocio del sistema
│   ├── entities/            Modelos centrales e independientes (User, Ticket, Session, Interaction)
│   └── repositories/        Interfaces y contratos abstractos de acceso a datos (sin código de BD)
├── application/             Capa de Aplicación: Casos de uso y orquestación
│   └── use_cases/           Flujos de negocio (ej. CrearTicket, ConsultarEstado, AutenticarUsuario)
├── infrastructure/          Capa de Infraestructura: Implementaciones concretas de servicios externos
│   ├── repositories/        Implementación de los contratos (consultas a MySQL, Redis, GLPI DB)
│   └── integrations/        Clientes de APIs externas (Zulip REST, Telegram, WhatsApp, RustDesk execution)
├── presentation/            Capa de Presentación: Entrada y salida de información del bot
│   ├── handlers/            Procesadores de eventos entrantes desde Redis o Webhooks
│   └── formatters/          Constructores de mensajes y plantillas de respuesta por plataforma
├── database/                Módulo existente: Configuración, scripts de migración y conexión de BD
├── models/                  Módulo existente: Data classes y enumeradores del sistema (Enums de tickets, comandos)
├── settings/                Módulo existente: Variables de entorno, secretos y configuración global
├── media/                   Módulo existente: Almacenamiento local de assets, imágenes y documentos
└── scripts/                 Módulo existente: Automatizaciones, utilidades de despliegue y scripts de soporte (Python/Unix/Windows)
```

## Direccion de dependencias

- `presentation` llama a `application`.
- `application` depende de contratos de `domain`.
- `infrastructure` implementa esos contratos.
- `domain` no debe depender de Zulip, MySQL ni detalles de infraestructura.

La migracion de la logica de `soporte.py` puede hacerse gradualmente en ese orden,
sin cambiar el punto de entrada actual hasta que cada caso de uso este probado.
