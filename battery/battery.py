from abc import ABC, abstractmethod

# abstract class
class Battery(ABC):

    @abstractmethod
    def needs_service(self):
        pass
