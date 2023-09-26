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

Robot_A=Robot()
Human_A=Human()

Robot_A.work()
Robot_A.eat()
Human_A.work()
Human_A.eat()
