Les principes SOLID sont un ensemble de cinq principes de conception logicielle qui visent à créer des systèmes logiciels bien structurés, faciles à comprendre, à maintenir et à étendre. Voici une brève explication de chacun de ces principes, accompagnée d'exemples en Python :

1. **Principe de responsabilité unique (Single Responsibility Principle - SRP)** : Une classe ne devrait avoir qu'une seule raison de changer.

   Exemple en Python :
   
   ```python
   class FileManager:
       def read_file(self, file_name):
           # Code pour lire un fichier
   
       def write_file(self, file_name, data):
           # Code pour écrire dans un fichier
   ```

   Dans cet exemple, la classe `FileManager` a deux responsabilités : lire et écrire des fichiers. Il serait préférable de diviser ces responsabilités en deux classes distinctes pour respecter le SRP.

2. **Principe d'ouverture/fermeture (Open/Closed Principle - OCP)** : Les entités (classes, modules, fonctions, etc.) doivent être ouvertes à l'extension mais fermées à la modification.

   Exemple en Python :
   
   ```python
   class Shape:
       def area(self):
           pass

   class Rectangle(Shape):
       def __init__(self, width, height):
           self.width = width
           self.height = height

       def area(self):
           return self.width * self.height

   class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius

       def area(self):
           return 3.14 * self.radius * self.radius
   ```

   Ici, de nouvelles formes peuvent être ajoutées (extension) sans modifier la classe `Shape` existante (fermeture).

3. **Principe de substitution de Liskov (Liskov Substitution Principle - LSP)** : Les objets d'une sous-classe doivent pouvoir être utilisés à la place des objets de la classe parente sans altérer la cohérence du programme.

   Exemple en Python :
   
   ```python
   class Bird:
       def fly(self):
           pass

   class Sparrow(Bird):
       def fly(self):
           print("Sparrow can fly")

   class Penguin(Bird):
       def fly(self):
           print("Penguin can't fly")
   ```

   Les classes `Sparrow` et `Penguin` sont des sous-classes de `Bird`, et elles respectent le principe de substitution de Liskov car elles peuvent être utilisées de manière interchangeable avec `Bird`.

4. **Principe de ségrégation de l'interface (Interface Segregation Principle - ISP)** : Il vaut mieux avoir plusieurs interfaces spécifiques qu'une interface générale.

   Exemple en Python :
   
   ```python
   from abc import ABC, abstractmethod

   class Worker(ABC):
       @abstractmethod
       def work(self):
           pass

       @abstractmethod
       def eat(self):
           pass

   class Robot(Worker):
       def work(self):
           print("Robot is working")

       def eat(self):
           print("Robot can't eat")

   class Human(Worker):
       def work(self):
           print("Human is working")

       def eat(self):
           print("Human is eating")
   ```

   Plutôt que d'avoir une interface générale `Worker`, nous avons des interfaces spécifiques `Robot` et `Human` qui ne forcent pas les classes à implémenter des méthodes inutiles.

5. **Principe d'inversion de dépendance (Dependency Inversion Principle - DIP)** : Les modules de haut niveau ne doivent pas dépendre des modules de bas niveau. Les deux devraient dépendre d'abstractions. De plus, les abstractions ne doivent pas dépendre des détails, mais les détails doivent dépendre des abstractions.

   Exemple en Python :
   
   ```python
   class Switchable(ABC):
       @abstractmethod
       def turn_on(self):
           pass

       @abstractmethod
       def turn_off(self):
           pass

   class LightBulb(Switchable):
       def turn_on(self):
           print("Light bulb turned on")

       def turn_off(self):
           print("Light bulb turned off")

   class Fan(Switchable):
       def turn_on(self):
           print("Fan turned on")

       def turn_off(self):
           print("Fan turned off")

   class ElectricPowerSwitch:
       def __init__(self, device):
           self.device = device
           self.state = False

       def press(self):
           if self.state:
               self.device.turn_off()
               self.state = False
           else:
               self.device.turn_on()
               self.state = True
   ```

   Le `ElectricPowerSwitch` dépend de l'abstraction `Switchable`, ce qui permet de changer facilement le dispositif connecté sans modifier le commutateur lui-même.

Ces principes SOLID sont conçus pour améliorer la qualité du code en le rendant plus modulaire, flexible et maintenable. En les suivant, vous pouvez concevoir des logiciels plus robustes et faciles à maintenir en Python ou dans tout autre langage de programmation.