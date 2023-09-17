# Bucles 

# While

""" my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # El while tiene la opción de agregar un else.
    print("Mi condicion es mayor o igual que 10")

print('La ejecución continúa')

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Se detiene la ejecucion')
        break #detiene la ejecución.
    print(my_condition)
    
print('La ejecución continúa') """


# For

""" my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)   
    
my_tuple = (23, 1.93, "Nicolas", "Rios", "Nico")
for element in my_tuple:
    print(element)   

my_set = {"Nicolas", "Rios", 23}
for element in my_set:
    print(element)    """

my_dict = {"Nombre": "Nicolas", "Apellido": "Rios", "Edad": 23}

for element in my_dict:
    print(element)
    if element == "Apellido":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")   

