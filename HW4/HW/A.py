class SpaceObject:
    def __init__(self, name):
        self.name = name


class Planet(SpaceObject):
    def __init__(self, name, population=None):
        super().__init__(name)
        self.population = population or []

    def __str__(self):
        return f'На планете {self.name} обитает {len(self.population)} тварей:\n'


class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def settling(self, planet):
        planet.population.append(self)


class Manul(Animal):
    def __init__(self, name, colour=None, sex=None):
        Animal.__init__(self, name)
        self.colour = colour
        self.sex = sex
        self.disregard = 0
        self.hiss = 0

    def lie(self, amount=30):
        self.disregard += amount
        print(f"Манул {self.name} обронил около {amount} единиц уважения")

    def anger(self):
        self.hiss += 1
        print(f"Манул {self.name} пошипел {self.hiss} раз")


class BrownPanda(Animal):
    def __init__(self, name, sex=None):
        Animal.__init__(self, name)
        self.sex = sex
        self.skills = 0

    def martial_arts(self):
        self.skills += 1
        print(f"Панда обрела +{self.skills} мастерства")


class Oriole(Animal):
    def __init__(self, name, song='warble', colour=None):
        Animal.__init__(self, name)
        self.colour = colour
        self.song = song
        self.fear = False

    def be_afraid(self):
        self.fear = True

    def singing(self, song='warble'):
        print(f"Иволга {self.name} побаивается") if self.fear else print(f"Иволга {self.name} пропела {song}")


earth = Planet('Earth')
manul_cats = [Manul('Pumba', 'sandy', 'male'),
              Manul('Frosya', 'gray', 'female')]
brown_pandas = [BrownPanda('Ademar', 'male'), BrownPanda('Fenissa', 'female')]
orioles = [Oriole('Enida', 'warble', 'blue')]

animals = [manul_cats, brown_pandas, orioles]

for item in animals:
    for animal in item:
        animal.settling(earth)

print(earth)
