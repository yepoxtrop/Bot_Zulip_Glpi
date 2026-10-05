# ARQUITECTURA

La arquitectura de software que se está usando para el proyecto es la **Arquitectura Hexagonal**.
**[NOTA]:**El Núcleo (Core) no conoce NADA del mundo exterior.

```text
src/
├── adapters/
├── application/            Capa de Aplicación: Casos de uso
└── logs                    Logs del aplicativo
```