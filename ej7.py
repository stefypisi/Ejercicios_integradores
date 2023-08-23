#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:  Un constructor, donde los datos pueden estar vacíos.  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.  mostrar(): Muestra los datos de la cuenta.  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad
        
    def get_cantidad(self):
        return self.__cantidad
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad
    
    def mostrar(self):
        print("Titular:", self.titular.nombre)
        print("Cantidad:", self.__cantidad)

# Solicitar los datos del titular al usuario
nombre_titular = input("Ingrese el nombre del titular: ")
titular_usuario = Persona(nombre_titular)

# Crear una cuenta con los datos ingresados
cuenta_usuario = Cuenta(titular_usuario)

# Mostrar los datos de la cuenta
print("\nDatos de la cuenta:")
cuenta_usuario.mostrar()

# Realizar operaciones en la cuenta
monto_ingreso = float(input("\nIngrese el monto a ingresar: "))
cuenta_usuario.ingresar(monto_ingreso)

monto_retiro = float(input("Ingrese el monto a retirar: "))
cuenta_usuario.retirar(monto_retiro)

# Mostrar los datos actualizados de la cuenta
print("\nDatos de la cuenta después de operaciones:")
cuenta_usuario.mostrar()