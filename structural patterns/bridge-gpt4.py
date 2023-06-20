#Dans cet exemple, DrawingAPI est l'interface d'implémentation, DrawingAPI1 et DrawingAPI2 sont ses implémentations concrètes. Shape est l'abstraction et CircleShape est l'abstraction raffinée.

#Les méthodes dans CircleShape (draw et resize_by_percentage) sont indépendantes de l'API de dessin utilisée. Cette dépendance est établie dynamiquement lors de l'instanciation des objets CircleShape.

from abc import ABC, abstractmethod

# Classe d'implémentation
class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass

# ConcreteImplementation 1
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at {x}:{y} radius {radius}")

# ConcreteImplementation 2
class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2.circle at {x}:{y} radius {radius}")

# Classe d'abstraction
class Shape(ABC):
    def __init__(self, drawing_api: DrawingAPI):
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize_by_percentage(self, pct):
        pass

# RefinedAbstraction 1
class CircleShape(Shape):
    def __init__(self, x, y, radius, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self._x = x
        self._y = y
        self._radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self._x, self._y, self._radius)

    def resize_by_percentage(self, pct):
        self._radius *= pct

# Program/Main
def main():
    shapes = [
        CircleShape(1, 2, 3, DrawingAPI1()),
        CircleShape(5, 7, 11, DrawingAPI2())
    ]

    for shape in shapes:
        shape.resize_by_percentage(2.5)
        shape.draw()

if __name__ == "__main__":
    main()
