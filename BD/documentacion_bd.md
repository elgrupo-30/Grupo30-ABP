# Documentación del Diseño de Base de Datos

## Tabla `roles`
- **Descripción**: Almacena los diferentes roles de usuarios del sistema
- **Atributos**:
  - `id`: Identificador único (PK)
  - `nombre`: Nombre del rol (único)
  - `descripcion`: Descripción del rol
  - `fecha_creacion`: Fecha de creación del rol
- **Suposiciones**: 
  - Se asume que los roles son predefinidos y no creados dinámicamente
  - Relación 1:N con usuarios (un rol puede tener muchos usuarios)

## Tabla `usuarios`
- **Descripción**: Almacena la información de los usuarios del sistema
- **Atributos**:
  - `id`: Identificador único (PK)
  - `nombre`: Nombre completo del usuario
  - `email`: Correo electrónico (único)
  - `contraseña_hash`: Hash de la contraseña (se asume algoritmo SHA-256)
     La columna contraseña_hash almacena contraseñas hasheadas con SHA-256
    
     Ejemplo: 'admin123' → '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
    
     Se utiliza este algoritmo porque:
    
      1. Es resistente a colisiones
      2. Genera un hash de 64 caracteres (256 bits)
      3. Es ampliamente utilizado y considerado seguro
  - `fecha_registro`: Fecha de registro del usuario
  - `rol_id`: Referencia al rol del usuario (FK)
- **Validaciones**:
  - El email debe ser único
  - La contraseña debe almacenarse como hash
  - Todo usuario debe tener un rol asignado

## Normalización (3FN)
- **1FN**: Todos los atributos son atómicos, no hay grupos repetitivos
- **2FN**: Cumple porque todos los atributos no clave dependen completamente de la PK
- **3FN**: Cumple porque no hay dependencias transitivas (los atributos no clave no dependen de otros atributos no clave)
