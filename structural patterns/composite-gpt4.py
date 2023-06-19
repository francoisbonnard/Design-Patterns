# Dans cet exemple, Component est la classe de base pour Leaf et Composite. Leaf est un élément 
# final qui ne peut pas avoir d'enfants, tandis que Composite est un élément qui peut avoir des
# enfants. Composite stocke des références à ses enfants et implémente des méthodes qui leur 
# permettent d'ajouter ou de supprimer des enfants. Le code du client peut traiter à la fois les 
# feuilles et les composites de manière uniforme.

from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @abstractmethod
    def operation(self) -> str:
        """
        A base operation that must be implemented by all concrete components
        and composite components. 
        """
        pass

class Leaf(Component):
    """
    Leaf represents the end object of a composition. A leaf can't have any
    children.
    """

    def operation(self) -> str:
        return "Leaf"

class Composite(Component):
    """
    Composite stores child components and implements child related operations in
    the component interface.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its child components, collecting and
        returning their results. Since the composite's children pass these calls
        to their children and so forth, the whole object tree is traversed as a
        result.
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """

    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex
