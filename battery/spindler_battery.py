from battery import Battery


# Spindler Battery - should be serviced once every 2 years
# UPDATE Spindler Battery - should be serviced once every 3 years
class Spindler(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date - self.last_service_date >= 3)
