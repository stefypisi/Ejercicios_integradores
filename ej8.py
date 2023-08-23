

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    def es_titular_valido(self):
        edad_actual = 2023 - int(self.titular.nombre.split()[-1])  # Se asume que el año de nacimiento está al final del nombre
        return 18 <= edad_actual < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede realizar el retiro. Titular no válido.")
    
    def mostrar(self):
        super().mostrar()
        print("Tipo de cuenta: Cuenta Joven")
        print("Bonificación:", self.__bonificacion, "%")

# Solicitar los datos del titular al usuario
nombre_titular = input("Ingrese el nombre completo del titular: ")
titular_usuario = Persona(nombre_titular)

# Solicitar datos específicos de Cuenta Joven al usuario
bonificacion = float(input("Ingrese el porcentaje de bonificación para la cuenta joven: "))
cuenta_joven_usuario = CuentaJoven(titular_usuario, bonificacion=bonificacion)

# Mostrar los datos de la cuenta joven
print("\nDatos de la cuenta joven:")
cuenta_joven_usuario.mostrar()

# Realizar operaciones en la cuenta joven
monto_ingreso = float(input("\nIngrese el monto a ingresar: "))
cuenta_joven_usuario.ingresar(monto_ingreso)

if cuenta_joven_usuario.es_titular_valido():
    monto_retiro = float(input("Ingrese el monto a retirar: "))
    cuenta_joven_usuario.retirar(monto_retiro)
else:
    print("El titular no es válido para realizar retiros.")

# Mostrar los datos actualizados de la cuenta joven
print("\nDatos de la cuenta joven después de operaciones:")
cuenta_joven_usuario.mostrar()
