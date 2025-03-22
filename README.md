# JumpingKids

JumpingKids es una aplicación que tiene el propósito de estimular a niños entre 10 y 15 años de edad a realizar actividades físicas que favorezcan su desarrollo.

Para participar en el proyecto es necesario entender la arquitectura y la forma en la que este proyecto puede funcionar. Puedes iniciar este proyecto en tu máquina siguiendo el siguiente tutorial sobre ambientación. Si ya tienes experiencia con GitHub Codespaces te será aún más fácil pero incluso para los iniciantes, el uso de este proyecto como Codespace agiliza el poner el marcha un proyecto.

# Inicio rápido

writing [...]
<!-- - Variables de entorno
- Se está usando una base de datos SQLite
- Se usa SQLAlchemy
- Se usa Poetry -->

# Arquitectura del Proyecto

Para contribuir al proyecto JumpingKids, es importante entender su arquitectura. El proyecto sigue los principios de la **Arquitectura Hexagonal**, que proporciona una separación clara entre la lógica de negocio y los detalles técnicos.

### Estructura del Proyecto

```
jumpingkids/
├── hexagon/                # Núcleo de la aplicación
│   ├── domain/             # Modelos de dominio y reglas de negocio
│   │   └── model.py        # Entidades principales (Routine, Exercise, etc.)
│   └── application/        # Casos de uso y servicios
│       └── service.py      # Interfaces de servicio (ports)
├── infrastructure/         # Implementaciones técnicas
│   ├── persistence/        # Acceso a datos y repositorios
│   └── adapter/            # Adaptadores entre capas
├── ui/                     # Interfaz de usuario
│   ├── view/               # Vistas de Flet
│   ├── controller/         # Controladores de vista
│   └── event/              # Manejadores de eventos
└── main.py                 # Punto de entrada de la aplicación
```

### Conceptos Clave

1. **Modelo de Dominio**: Las clases en `hexagon/domain/model.py` representan las entidades principales y reglas de negocio.

2. **Puertos**: Interfaces en `hexagon/application/service.py` que definen lo que la aplicación puede hacer, y exponer al mundo.

3. **Adaptadores**: Implementaciones concretas de los puertos en `infrastructure/`.

4. **Patrón MVC en UI**: 
   - **Modelo**: Datos del dominio
   - **Vista**: Componentes Flet en `ui/view/`
   - **Controlador**: Clases en `ui/controller/` que manejan la lógica de la UI

### Flujo de Datos

1. La UI solicita datos o acciones a través de los controladores
2. Los controladores utilizan los servicios del dominio (puertos)
3. Los servicios implementan la lógica de negocio y usan repositorios
4. Los repositorios acceden a la base de datos y devuelven resultados

### Añadir Nuevas Funcionalidades

Para añadir una nueva funcionalidad:

1. Define los modelos necesarios en el dominio en caso de que las definiciones actuales no satisfagan los requisitos.
2. Crea, extiende o usa los puertos de servicio necesarios
3. Implementa los adaptadores correspondientes
4. Crea la vista en Flet
5. Implementa el controlador para conectar la vista con los servicios
6. Conecta los eventos de la vista con los métodos del controlador
7. Haz que `AppBuilder` reconozca tu nueva vista construida, en caso de hayas construido una, de lo contrario, asegurate de que la organización de las vistas actuales se mantenga y pueda implementar fácilmente tus constribuciones.
