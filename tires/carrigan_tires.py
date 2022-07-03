from tires import Tires


# Carrigan tires - should be serviced only when one or more of the values in the tire wear array is greater than or equal to 0.9.
class CarriganTires(Tires):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        return not (all(i < 0.9 for i in self.tire_array))

        # for i in self.tire_array:
        #     if i < 0.9:
        #         return True
        #