#Dans cet exemple, le Director est en charge de la construction d'un Car qui est un objet complexe. 
# Le processus de construction est délégué à un objet Builder, qui est SkyLarkBuilder dans ce cas. 
# Le Director n'a pas besoin de savoir quel type de Car il construit, comment les pièces sont 
# assemblées ou comment l'objet est structuré. Cela signifie que vous pouvez changer le Builder
# pour créer un Car différent sans avoir à modifier le Director.

class Director:
    def __init__(self):
        self._builder = None

    def builder(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

class Builder:
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):
    def add_model(self):
        self.car.model = "SkyLark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"

class Car:
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return f'{self.model} | {self.tires} | {self.engine}'

director = Director()
director.builder(SkyLarkBuilder())
director.construct_car()
car = director._builder.car
print(car)
