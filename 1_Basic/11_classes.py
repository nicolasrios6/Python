# Clases

class OtherPerson:
    pass

print(OtherPerson )

class Person:
    def __init__ (self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} { surname} ({alias})"
        self.__name = name #propiedad definida como privada
        
    def get_name(self):
        return self.__name
        
    def walk(self):
        print(f"{self.full_name} está caminando")
    
my_person = Person("Nicolas", "Rios")
print(f"{my_person.full_name}")
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Pepe", "Baco", "Pichito")
print(f"{my_other_person.full_name}")
my_other_person.walk()
my_other_person.full_name = "Julian Alvarez Araña"
print(f"{my_other_person.full_name}")
