from engine import Engine

# Willoughby Engine - should be serviced once every 60,000 miles
class Willoughby(Engine):
  def __init__(self, last_service_mileage, current_mileage):
    self.last_service_mileage = last_service_mileage
    self.current_mileage = current_mileage

  def needs_service(self):
    return (self.current_mileage - self.last_service_mileage > 60000)

