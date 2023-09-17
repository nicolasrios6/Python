# Funciones

def my_function ():
    print('Esto es una funcion')
    
my_function()

def suma (num1, num2):
    print(num1 + num2)
    
suma(2,4)

def suma_con_return (num1, num2):
	return num1 + num2

resultado = suma_con_return(10, 5)
print(resultado)

def mostrar_nombre(nombre, apellido):
    print(f'Hola {nombre} {apellido}, como estas?')
    
mostrar_nombre(apellido = "Rios",nombre = "Nicolas")


def mostrar_nombre_default(nombre, apellido, alias = "Sin alias"):
    print(f'Hola {nombre} {apellido} {alias}, como estas?')
    
mostrar_nombre_default("Nicolas", "Rios")

def mostrar_textos(*text):
    print(text)
    
mostrar_textos("Hola", "blabla", "fsdfsd")