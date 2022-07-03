from engine import Engine


# Sternman Engine - should be serviced once every 30,000 miles
class Sternman(Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return self.warning_light_on

