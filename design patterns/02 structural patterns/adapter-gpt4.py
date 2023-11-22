# Dans cet exemple, nous avons une prise européenne (Socket) qui est l'adaptée. Nous avons une interface de prise américaine (USASocketInterface) qui est l'interface cible. L'adaptateur (Adapter) transforme l'interface de la prise européenne en une interface de prise américaine.

# Lorsque la bouilloire électrique (le client) tente de faire bouillir de l'eau, elle utilise l'interface de prise américaine. Cependant, grâce à l'adaptateur, elle peut fonctionner avec une prise européenne.

class EuropeanSocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass
    def earth(self): pass

# Adaptee
class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230
    def live(self):
        return 1
    def neutral(self):
        return -1
    def earth(self):
        return 0

# Target interface
class USASocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass

# The Adapter
class Adapter(USASocketInterface):
    __socket = None
    def __init__(self, socket):
        self.__socket = socket
    def voltage(self):
        return 110
    def live(self):
        return self.__socket.live()
    def neutral(self):
        return self.__socket.neutral()

# Client
class ElectricKettle:
    __power = None
    def __init__(self, power):
        self.__power = power
    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle on fire!")
        elif self.__power.live() == 1 and \
             self.__power.neutral() == -1:
            print("Coffee time!")
        else:
            print("No power.")

def main():
    # Plug in
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    # Make coffee
    kettle.boil()

if __name__ == "__main__":
    main()
``
