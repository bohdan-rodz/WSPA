class Osoba:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

person1 = Osoba("John", "Cena", 15)
print(person1.name + " " + person1.surname)