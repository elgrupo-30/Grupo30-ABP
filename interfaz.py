from usuarios import GestorUsuarios

class InterfazConsola:
    def __init__(self):
        self.gestor = GestorUsuarios()

    def mostrar_menu_principal(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self._manejar_inicio_sesion()
            elif opcion == "2":
                self._manejar_registro()
            elif opcion == "3":
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida")

    def _manejar_inicio_sesion(self):
        email = input("Email: ")
        contraseña = input("Contraseña: ")
        
        usuario = self.gestor.iniciar_sesion(email, contraseña)
        if usuario:
            print(f"\nBienvenido, {usuario.nombre}!")
            if usuario.rol == "admin":
                self.mostrar_menu_admin()
            else:
                self.mostrar_menu_usuario(usuario)
        else:
            print("Credenciales incorrectas")

    def _manejar_registro(self):
        nombre = input("Nombre completo: ")
        email = input("Email: ")
        contraseña = input("Contraseña (mínimo 6 caracteres con letras y números): ")
        
        if self.gestor.registrar_usuario(nombre, email, contraseña):
            print("¡Registro exitoso!")
        else:
            print("Error: Email inválido o ya registrado")

    def mostrar_menu_admin(self):
        while True:
            print("\n--- MENÚ ADMINISTRADOR ---")
            print("1. Ver todos los usuarios")
            print("2. Eliminar usuario")
            print("3. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                usuarios = self.gestor.obtener_todos_usuarios()
                for usuario in usuarios:
                    print(f"ID: {usuario['id']} - {usuario['nombre']} ({usuario['email']})")
            
            elif opcion == "2":
                id_usuario = int(input("ID del usuario a eliminar: "))
                if self.gestor.eliminar_usuario(id_usuario):
                    print("Usuario eliminado")
                else:
                    print("ID no encontrado")
            
            elif opcion == "3":
                break
            
            else:
                print("Opción no válida")

    def mostrar_menu_usuario(self, usuario):
        while True:
            print("\n--- MENÚ USUARIO ---")
            print("1. Ver mis datos")
            print("2. Cambiar contraseña")
            print("3. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                datos = usuario.mostrar_datos()
                for clave, valor in datos.items():
                    print(f"{clave.capitalize()}: {valor}")
            
            elif opcion == "2":
                nueva_contraseña = input("Nueva contraseña: ")
                if usuario.cambiar_contraseña(nueva_contraseña):
                    print("Contraseña actualizada")
                else:
                    print("Contraseña no válida")
            
            elif opcion == "3":
                break
            
            else:
                print("Opción no válida")