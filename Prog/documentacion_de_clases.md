# Documentación de Clases

## Clase Usuario

### Descripción
Representa a un usuario del sistema con sus datos personales y funcionalidades de autenticación.

### Atributos
| Nombre           | Tipo   | Visibilidad | Descripción                              |
|------------------|--------|-------------|------------------------------------------|
| `id_usuario`     | int    | pública     | Identificador único del usuario          |
| `nombre`         | str    | pública     | Nombre completo del usuario              |
| `email`          | str    | pública     | Correo electrónico                       |
| `_contraseña`    | str    | protegida   | Hash de la contraseña (SHA-256)          |
| `rol`            | str    | pública     | Rol del usuario (admin/usuario)          |
| `fecha_registro` | str    | pública     | Fecha de registro en formato ISO 8601    |

### Métodos

#### `verificar_contraseña(contraseña: str) -> bool`
Verifica si una contraseña en texto plano coincide con el hash almacenado.

**Parámetros:**
- `contraseña`: Contraseña a verificar (texto plano)

**Retorno:**
- `True` si coinciden, `False` en caso contrario

---

#### `cambiar_contraseña(nueva_contraseña: str) -> bool`
Cambia la contraseña del usuario si cumple con los requisitos de seguridad.

**Parámetros:**
- `nueva_contraseña`: Nueva contraseña a establecer

**Retorno:**
- `True` si se cambió exitosamente, `False` si no cumple requisitos

---

#### `mostrar_datos() -> dict`
Devuelve un diccionario con los datos públicos del usuario.

**Retorno:**
```python
{
    "id": int,
    "nombre": str,
    "email": str,
    "rol": str,
    "fecha_registro": str
}
```

---

## Clase GestorUsuarios

### Descripción
Gestiona el registro y autenticación de usuarios en el sistema.

### Atributos
| Nombre    | Tipo           | Visibilidad | Descripción                      |
|-----------|----------------|-------------|----------------------------------|
| `usuarios`| List[Usuario]  | privada     | Lista de usuarios registrados    |

### Métodos

#### `registrar_usuario(nombre: str, email: str, contraseña: str, rol: str = "usuario") -> bool`
Registra un nuevo usuario en el sistema.

**Parámetros:**
- `nombre`: Nombre completo  
- `email`: Correo electrónico  
- `contraseña`: Contraseña en texto plano  
- `rol`: Rol del usuario (opcional, default: `"usuario"`)

**Retorno:**
- `True` si se registró exitosamente  
- `False` si el email es inválido o ya existe

---

#### `iniciar_sesion(email: str, contraseña: str) -> Optional[Usuario]`
Autentica a un usuario en el sistema.

**Parámetros:**
- `email`: Correo electrónico  
- `contraseña`: Contraseña en texto plano  

**Retorno:**
- Objeto `Usuario` si las credenciales son válidas  
- `None` si la autenticación falla

---

#### `obtener_todos_usuarios() -> List[dict]`
Obtiene los datos de todos los usuarios registrados.

**Retorno:**
```python
[
    {
        "id": int,
        "nombre": str,
        "email": str,
        "rol": str,
        "fecha_registro": str
    },
    ...
]
```

---

#### `eliminar_usuario(id_usuario: int) -> bool`
Elimina un usuario del sistema por su ID.

**Parámetros:**
- `id_usuario`: ID del usuario a eliminar

**Retorno:**
- `True` si se eliminó exitosamente  
- `False` si no se encontró el usuario

---

## Clase InterfazConsola

### Descripción
Provee una interfaz de línea de comandos para interactuar con el sistema.

### Atributos
| Nombre   | Tipo           | Visibilidad | Descripción                      |
|----------|----------------|-------------|----------------------------------|
| `gestor` | GestorUsuarios | privada     | Instancia del gestor de usuarios|

### Métodos principales

#### `mostrar_menu_principal()`
Muestra el menú principal con opciones de:
- Iniciar sesión  
- Registrarse  
- Salir

---

#### `mostrar_menu_admin()`
Muestra el menú exclusivo para administradores con opciones de:
- Ver todos los usuarios  
- Eliminar usuario  
- Salir

---

#### `mostrar_menu_usuario(usuario: Usuario)`
Muestra el menú para usuarios normales con opciones de:
- Ver mis datos  
- Cambiar contraseña  
- Salir

---

## Clase Autenticador (Estática)

### Descripción
Provee métodos estáticos para validación y seguridad de credenciales.

### Métodos estáticos

#### `validar_email(email: str) -> bool`
Valida el formato de un correo electrónico.  
Regex utilizado: `^[\w\.-]+@[\w\.-]+\.\w+$`

---

#### `validar_contraseña(contraseña: str) -> bool`
Valida que una contraseña cumpla con:
- Mínimo 6 caracteres  
- Al menos una letra  
- Al menos un número

---

#### `generar_hash(texto: str) -> str`
Genera un hash SHA-256 en hexadecimal.

---

#### `verificar_hash(texto: str, hash_almacenado: str) -> bool`
Compara un texto plano con un hash almacenado.