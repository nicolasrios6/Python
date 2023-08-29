# Lists

my_list = list()
my_other_list = []

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [23, 1.92, 'Nico', 'Rios']
print(my_other_list)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count(23)) # Devuelve cuantas veces aparece el valor en la lista

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)

# my_list = "Hola Python"
# print(my_list)

my_other_list.append("Baco")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = 'Verde'
print(my_other_list)

# my_other_list.remove("Rojo")
# print(my_other_list)

print(my_list.pop())
print(my_list.pop(2))

del my_list[2]

my_new_list = my_list.copy()
print(my_new_list)
my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list.clear()
print(my_list)

