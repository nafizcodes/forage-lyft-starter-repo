from abc import ABC, abstractmethod

class Tires(ABC):
    def __int__(self, tire_array):
        self.tire_array = tire_array

    @abstractmethod
    def need_service(self):
        pass