# Operadores Aritmeticos

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 4)
print(10 // 3) # Floor Division: Resultado aproximado a un int
print(2 ** 3) # Exponente: base ** exponente

# Suma de strings
print('Hola ' + 'Python ' + 'como va?')

# print('Hola ' + 5) No podemos mezclar los tipos
print('Hola ' + str(5)) 
print('Hola ' * 5) 
# print("Hola" / 2) No se puede

my_float = 2.5 * 2 # da 5.0
print("Hola " * int(my_float))

# Operadores Comparativos
# Devuelven un valor booleano
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print('Hola' > 'Python')
print('Hola' < 'Python')
print('aaa' >= 'aab') # Orden alfabetico por ASCII
print('Hola' <= 'Python')
print('Hola' == 'Hola')
print('Hola' != 'Python')

# Operadores Lógicos

print(3 > 4 and 'hola' > 'python')
print(3 < 4 or 'hola' > 'python')
print(not(3 > 4) ) # Se niega la condicion
