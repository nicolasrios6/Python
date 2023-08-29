# Variables

my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print()
print(my_string_variable, my_int_to_str_variable, my_bool_variable)

print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Nicolas", "Rios", "Nico", 23
print("Me llamo",name, surname,". Mi edad es:", age,"y mi alias es:", alias)

# Input (para ingresar datos)
nombre_usuario = input("Ingresa tu nombre: ")
print(nombre_usuario)