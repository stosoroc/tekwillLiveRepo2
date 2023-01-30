from abc import ABC, abstractmethod


class CarAbstract(ABC):

    @abstractmethod
    def drive(self):
        print('Brrr')


class Bus(CarAbstract):

    def drive(self):
        # Must implement drive in Bus
        print('Brrrr')


bus = Bus()
bus.drive()
