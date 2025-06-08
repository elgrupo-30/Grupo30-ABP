import re
import hashlib

class Autenticador:
    @staticmethod
    def validar_email(email: str) -> bool:
        return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

    @staticmethod
    def validar_contraseña(contraseña: str) -> bool:
        return (
            len(contraseña) >= 6 and
            any(c.isalpha() for c in contraseña) and
            any(c.isdigit() for c in contraseña)
        )

    @staticmethod
    def generar_hash(contraseña: str) -> str:
        return hashlib.sha256(contraseña.encode()).hexdigest()

    @staticmethod
    def verificar_hash(contraseña: str, hash_almacenado: str) -> bool:
        return Autenticador.generar_hash(contraseña) == hash_almacenado