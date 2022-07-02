from battery import Battery

# Nubbin Battery - should be serviced once every 4 years
class Nubbin(Battery):
  def __init__(self, last_service_date, current_date):
    self.last_service_date = last_service_date
    self.current_date = current_date

  def needs_service(self):
        return (self.current_date - self.last_service_date >= 4)
