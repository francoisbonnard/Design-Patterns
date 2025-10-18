
## Polymorphism

Polymorphism in Python allows objects of different types to be treated as objects of a common type. There are two main types of polymorphism in Python: compile-time (or method overloading) and runtime (or method overriding). I'll provide an example of runtime polymorphism using method overriding.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Function that takes an Animal object and calls its speak method
def animal_sound(animal):
    return animal.speak()

# Creating instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the function with different animal objects
print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!
print(animal_sound(cow))  # Output: Moo!

```