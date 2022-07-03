from tires import Tires


# Octoprime tires - should be serviced only when the sum of all values in the tire wear array is greater than or equal to 3
class Octoprime(Tires):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        return sum(self.tire_array) >= 3