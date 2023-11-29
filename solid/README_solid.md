# Les principes SOLID 

Ensemble de cinq principes de conception logicielle qui visent à créer des systèmes logiciels bien structurés, faciles à comprendre, à maintenir et à étendre. Voici une brève explication de chacun de ces principes, accompagnée d'exemples en Python :

Single Responsibility Principle (SRP) : Une classe devrait avoir une seule raison de changer.

Open/Closed Principle (OCP) : Une classe devrait être ouverte à l'extension mais fermée à la modification.

Liskov Substitution Principle (LSP) : Les objets d'une classe de base doivent pouvoir être remplacés par des objets de classes dérivées sans affecter la cohérence du programme.

Interface Segregation Principle (ISP) : Il vaut mieux avoir plusieurs interfaces spécifiques qu'une interface générale.

Dependency Inversion Principle (DIP) : Les modules de haut niveau ne devraient pas dépendre des modules de bas niveau. Les deux devraient dépendre d'abstractions. De plus, les abstractions ne devraient pas dépendre des détails, mais les détails devraient dépendre des abstractions.

Lien avec les Design Patterns

Par exemple, le design pattern "Observer" peut être utilisé pour respecter le principe de responsabilité unique (SRP) en permettant à un objet d'avoir une seule responsabilité tout en permettant à d'autres objets d'observer ses changements d'état. De même, le design pattern "Strategy" peut être utilisé pour respecter le principe d'ouverture/fermeture (OCP) en permettant de changer dynamiquement le comportement d'un objet sans le modifier.

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

objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program

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

# Lien avec les design patterns

Les Design Patterns du Gang of Four (GoF) et les principes SOLID sont deux concepts importants en matière de conception logicielle, et ils sont liés de plusieurs façons.


1. Cohésion et Couplage :
   - Les principes SOLID, en particulier le principe de la Responsabilité Unique (Single Responsibility Principle - SRP), visent à promouvoir une forte cohésion dans les classes en s'assurant qu'elles ont une seule raison de changer. Les Design Patterns du GoF, tels que le "Pattern de Responsabilité Unique" (Single Responsibility Pattern), sont alignés avec le SRP et encouragent une conception avec des classes spécifiques ayant des responsabilités claires.
   - Le principe de Faible Couplage (Low Coupling) de SOLID, qui encourage à réduire les dépendances entre les classes, est également lié à de nombreux Design Patterns du GoF, car de nombreux patterns favorisent une faible couplage entre les composants logiciels.

2. Ouverture/Fermeture (Open/Closed Principle - OCP) :
   - Le principe OCP de SOLID encourage à concevoir des classes de manière à ce qu'elles puissent être étendues (ouvertes) sans nécessiter de modification de leur code source existant (fermées). Certains Design Patterns du GoF, tels que le "Pattern Stratégie" (Strategy Pattern) ou le "Pattern Observateur" (Observer Pattern), illustrent ce principe en permettant l'ajout de nouvelles fonctionnalités sans altérer le code existant.

3. Substitution de Liskov (Liskov Substitution Principle - LSP) :
   - Le principe LSP de SOLID stipule que les objets de sous-classes doivent pouvoir être utilisés sans que le code utilisateur ait besoin de connaître la différence entre les objets de ces sous-classes et les objets de la classe de base. Les Design Patterns du GoF, tels que le "Pattern Adapteur" (Adapter Pattern) ou le "Pattern Stratégie" (Strategy Pattern), implémentent souvent ce principe en permettant l'utilisation interchangeable d'objets.

4. Interface Ségrégation (Interface Segregation Principle - ISP) :
   - Le principe ISP de SOLID suggère que les interfaces doivent être spécifiques aux besoins des clients qui les utilisent, évitant ainsi les interfaces surchargées de méthodes inutiles. Certains Design Patterns du GoF, tels que le "Pattern Adapteur" (Adapter Pattern), peuvent être utilisés pour adapter une interface à une autre, respectant ainsi le principe d'ISP.

5. Dépendance Inversion Principle (DIP) :
   - Le principe DIP de SOLID encourage à dépendre des abstractions plutôt que des détails concrets. Certains Design Patterns du GoF, comme le "Pattern Fabrique Abstraite" (Abstract Factory Pattern) ou le "Pattern Décorateur" (Decorator Pattern), promeuvent l'inversion des dépendances en utilisant des interfaces ou des classes abstraites pour créer des familles d'objets ou ajouter des fonctionnalités.

En résumé, les Design Patterns du Gang of Four et les principes SOLID sont étroitement liés dans le domaine de la conception logicielle, car ils partagent des objectifs communs, tels que la création de code extensible, maintenable et évolutif. Les Design Patterns du GoF sont des solutions concrètes à des problèmes de conception courants, tandis que les principes SOLID fournissent des directives générales pour créer des architectures logicielles flexibles et robustes. L'utilisation appropriée des Design Patterns du GoF peut contribuer à la mise en œuvre des principes SOLID dans un système logiciel.