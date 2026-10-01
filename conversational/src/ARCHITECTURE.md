


# Estructura modular propuesta

Esta estructura agrega capas nuevas sin mover ni modificar los modulos actuales.

```text
src/
|-- domain/
|   |-- entities/       Entidades y estado del negocio
|   `-- repositories/   Contratos abstractos de persistencia
|-- application/
|   `-- use_cases/      Flujos de negocio del bot
|-- infrastructure/
|   |-- repositories/   Implementaciones para GLPI y base de datos
|   `-- integrations/   Adaptadores para Zulip, RustDesk y APIs externas
|-- presentation/
|   |-- handlers/       Entrada de mensajes y coordinacion del bot
|   `-- formatters/     Construccion de respuestas
|-- database/           Modulo existente, se conserva
|-- models/             Modulo existente, se conserva
|-- settings/           Modulo existente, se conserva
|-- media/              Modulo existente, se conserva
`-- scripts/            Modulo existente, se conserva
```

## Direccion de dependencias

- `presentation` llama a `application`.
- `application` depende de contratos de `domain`.
- `infrastructure` implementa esos contratos.
- `domain` no debe depender de Zulip, MySQL ni detalles de infraestructura.

La migracion de la logica de `soporte.py` puede hacerse gradualmente en ese orden,
sin cambiar el punto de entrada actual hasta que cada caso de uso este probado.
