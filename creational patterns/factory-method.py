# Dans cet exemple, le Creator est une classe abstraite qui déclare la méthode factory (factory_method). Les classes ConcreteCreator1 et ConcreteCreator2 sont des implémentations concrètes de Creator qui override factory_method pour retourner une instance de ConcreteProduct1 et ConcreteProduct2 respectivement.

# La fonction client_code illustre comment une instance de ConcreteCreator peut être utilisée. La fonction client_code n'a pas besoin de savoir quelle classe concrète de Creator elle utilise, car elle utilise uniquement les méthodes déclarées dans l'interface Creator.


from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"

def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
