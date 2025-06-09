# Sistema de Gestión de Usuarios 

Programa de consola para administración de usuarios con autenticación segura y control de roles (admin/usuario).

## Repositorio
🔗 [GitHub - Grupo30-ABP](https://github.com/elgrupo-30/Grupo30-ABP.git)

## Características Principales
- **Autenticación segura** con hashing SHA-256
- **Sistema de roles**: Admin y Usuario estándar
- **Validaciones robustas** de email y contraseña
- **Interfaz intuitiva** por consola
- **Diseño modular** para fácil mantenimiento

## Instalación
1. Clonar repositorio:
```bash
git clone https://github.com/elgrupo-30/Grupo30-ABP.git
cd Grupo30-ABP
Ejecutar:

bash
python main.py
Credenciales Iniciales
Rol	Email	Contraseña
Admin	admin@example.com	admin123

Funcionalidades por Rol
Función	              Admin  Usuario
Ver todos los usuarios	✅	❌
Eliminar usuarios	✅	❌
Ver datos personales	✅	✅
Cambiar contraseña	✅	✅
