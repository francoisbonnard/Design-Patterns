from abc import ABC, abstractmethod

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

Light = LightBulb()

Ventilo = Fan()

EP1 = ElectricPowerSwitch(Light)
EP2 = ElectricPowerSwitch(Ventilo)

EP1.press()
EP2.press()
EP2.press()
