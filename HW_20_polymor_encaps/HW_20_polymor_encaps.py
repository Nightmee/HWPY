class Man:

    def __init__(self,name,sleeping):
        self.name = name
        self.sleeping = sleeping

    def sleep(self):
        return f"Man is {self.sleeping}"

class Woman:

    def __init__(self,name, sleeping):
        self.name = name
        self.sleeping = sleeping

    def sleep(self):
        return f"Woman is {self.sleeping}"

Wasya = Man('Wasya','sleeping')
Vika = Woman('Vika','sleeping')
info_sleep = (Wasya, Vika)
for persons in info_sleep:
    print(persons.sleep())


print('#' * 40)

class Cat():

    def __init__(self, name, color, skill):
        """public"""
        self.name = name
        """protected"""
        self._color = color
        """private"""
        self.__skill = skill


    def eat(self):
        return F"{self.name} is eating"


    def color_c(self):
        return f"{self.name} is {self._color}"

    def skills(self):
        return f"{self.name} have good {self.__skill}"


Rita = Cat('Rita', 'white', 'sprint')
Rizik = Cat('Rizik', 'orange', 'eating food at speed')
print(Rita.eat())
print(Rita.color_c())
print(Rita.skills())

print('#' * 40)

print(Rizik.eat())
print(Rizik.color_c())
print(Rizik.skills())