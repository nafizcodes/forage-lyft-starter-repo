from abc import ABC, abstractmethod

# abstract class
class Engine(ABC):

    @abstractmethod
    def needs_service(self):
        pass
