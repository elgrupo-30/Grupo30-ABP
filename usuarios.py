from datetime import datetime
from autenticacion import Autenticador

class Usuario:
    def __init__(self, id_usuario: int, nombre: str, email: str, contraseña: str, rol: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self._contraseña = contraseña  # Hash almacenado
        self.rol = rol
        self.fecha_registro = datetime.now().isoformat()

    def verificar_contraseña(self, contraseña: str) -> bool:
        return Autenticador.verificar_hash(contraseña, self._contraseña)

    def cambiar_contraseña(self, nueva_contraseña: str) -> bool:
        if Autenticador.validar_contraseña(nueva_contraseña):
            self._contraseña = Autenticador.generar_hash(nueva_contraseña)
            return True
        return False

    def mostrar_datos(self) -> dict:
        return {
            "id": self.id_usuario,
            "nombre": self.nombre,
            "email": self.email,
            "rol": self.rol,
            "fecha_registro": self.fecha_registro
        }

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []
        self._crear_admin_inicial()

    def _crear_admin_inicial(self):
        admin = Usuario(
            id_usuario=1,
            nombre="Admin",
            email="admin@example.com",
            contraseña=Autenticador.generar_hash("admin123"),
            rol="admin"
        )
        self.usuarios.append(admin)

    def registrar_usuario(self, nombre: str, email: str, contraseña: str, rol: str = "usuario") -> bool:
        if not Autenticador.validar_email(email):
            return False
        
        if any(u.email == email for u in self.usuarios):
            return False

        nuevo_id = max(u.id_usuario for u in self.usuarios) + 1 if self.usuarios else 1
        nuevo_usuario = Usuario(
            id_usuario=nuevo_id,
            nombre=nombre,
            email=email,
            contraseña=Autenticador.generar_hash(contraseña),
            rol=rol
        )
        self.usuarios.append(nuevo_usuario)
        return True

    def iniciar_sesion(self, email: str, contraseña: str):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.verificar_contraseña(contraseña):
                return usuario
        return None

    def obtener_todos_usuarios(self):
        return [u.mostrar_datos() for u in self.usuarios]

    def eliminar_usuario(self, id_usuario: int) -> bool:
        for i, usuario in enumerate(self.usuarios):
            if usuario.id_usuario == id_usuario:
                self.usuarios.pop(i)
                return True
        return False