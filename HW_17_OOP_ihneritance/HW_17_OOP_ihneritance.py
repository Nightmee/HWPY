class Animal:
    info = 'Animal'

    def __init__(self, name_of_animal, color):
        self.name_of_animal = name_of_animal
        self.color = color


    def breath(self):
        return f"{self.name_of_animal} is breathing"

    def run(self):
        return f"{self.name_of_animal} is running"

    def clo(self):
        return f"{self.color}"


class Eagle(Animal):

    info = 'Desert Eagle'

    def __init__(self, name_of_animal, color):
        Animal.__init__(self, name_of_animal, color)
        self.name_of_animal = name_of_animal
        self.color = color


    def fly(self):
        return f"The Eagle have name {self.name_of_animal} and he can fly"


    def super_vision(self):
        return f"{self.name_of_animal} have good vision"


class Cat(Animal):

    info = 'Cat is always hungry'

    def __init__(self, name_of_animal, color):
        Animal.__init__(self, name_of_animal, color)
        self.name_of_animal = name_of_animal
        self.color = color

    def jump(self):
        return f"{self.name_of_animal} is jumping very high"


    def surprize(self, You):
        if You == 'go outside':
            return f"{self.name_of_animal} can make a surpize in your shoes"
        else:
            return f"You are lucky!!!!!!!!!!"


class Dragon(Cat, Eagle, Animal):

    info = 'Mutatation'

    def __init__(self, name_of_animal, color):
        self.name_of_animal = name_of_animal
        self.color = color


    def superskill(self):
        return f"{self.name_of_animal} can make a fire"



print('Is Eagle issubclass of Animal', issubclass(Animal, Animal))
print('Is Cat issubclass of Animal', issubclass(Animal, Animal))

Animal1 = Animal('Tiger', 'orange')
print(Animal1.breath())
print(Animal1.run())

Jack = Eagle('Jack', 'white')
print(Jack.fly())
print(Jack.super_vision())

Wasya = Cat('Wasya', 'Orange')
print(Wasya.breath())
print(Wasya.surprize('go outside'))

KitKat = Dragon('KitKat', 'Red')
print(KitKat.superskill())