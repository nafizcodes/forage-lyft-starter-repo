from abc import ABC, abstractmethod


# abstract class
class Service(ABC):

    @abstractmethod
    def needs_service(self):
        pass
