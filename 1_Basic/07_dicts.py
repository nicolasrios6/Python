# Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Nicolas", "Apellido": "Rios", "Edad": 23, 1: "Python"}
print(my_other_dict)

my_dict = {
    "Nombre": "Nicolas",
    "Apellido": "Rios",
    "Edad": 23,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.92
    }

print(my_dict)
print(len(my_dict))
print(my_dict['Nombre'])

my_dict['Nombre'] = 'Pepe' # modificar valores
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = 'Malabia' # agregar clave y valor
print(my_dict["Calle"])


# del my_dict["Calle"] # eliminar elemento
# print(my_dict)

print("Nombre" in my_dict) #busca por clave y no por valor

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("Nombre", 1, "Color"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,"Nico")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))