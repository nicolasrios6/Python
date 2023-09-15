# Excepciones

num1 = 5
num2 = 1
num2 = '1'

# try except
""" try:
    print(num1 + num2)
    print("No se ha producido un error")
except:
    # se ejecuta si se produce una excepcion
    print("Se ha producido un error") """
    
#try except else

""" try:
    print(num1 + num2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: 
    # se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:
    # se ejecuta siempre haya error o no
    print("La ejecucion continua") """
    
# Excepciones por tipo

""" try:
    print(num1 + num2)
    print("No se ha producido un error")
except ValueError:
    # se ejecuta si se produce una excepcion
    print("Se ha producido un ValueError")
except TypeError:
    # se ejecuta si se produce una excepcion
    print("Se ha producido un TypeError") """
    
# Captura de la informacion de la excepcion
try:
    print(num1 + num2)
    print("No se ha producido un error")
except TypeError as error:
    # se ejecuta si se produce una excepcion
    print(error)
except Exception as error:
    print(error)