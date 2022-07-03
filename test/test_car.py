import unittest
from datetime import datetime

# Engines
from engine.capulet_engine import Capulet
from engine.willoughby_engine import Willoughby
from engine.sternman_engine import Sternman

# Batteries
from battery.spindler_battery import Spindler
from battery.nubbin_battery import Nubbin

#Tires
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import Octoprime


class TestEngines(unittest.TestCase):
    # Capulet Engine - should be serviced once every 30,000 miles
    def test_capulet_engine_should_be_service(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = Capulet(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_should_not_be_service(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = Capulet(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

    # Willoughby Engine - should be serviced once every 60,000 miles
    def test_willoughby_engine_should_be_service(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = Willoughby(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_should_not_be_service(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = Willoughby(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

    # Sternman Engine - should be serviced only when the warning indicator is on
    def test_sternman_engine_should_be_service(self):
        warning_light_on = True

        engine = Sternman(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_should_not_be_service(self):
        warning_light_on = False

        engine = Sternman(warning_light_on)
        self.assertFalse(engine.needs_service())


class TestBattery(unittest.TestCase):
    # Spindler Battery - should be serviced once every 2 years
    # UPDATE Spindler Battery - should be serviced once every 3 years
    def test_spindler_battery_should_be_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        battery = Spindler(last_service_date.year, current_date.year)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = Spindler(last_service_date.year, current_date.year)
        self.assertFalse(battery.needs_service())

    # Nubbin Battery - should be serviced once every 4 years
    def test_nubbin_battery_should_be_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        battery = Nubbin(last_service_date.year, current_date.year)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_be_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)

        battery = Nubbin(last_service_date.year, current_date.year)
        self.assertFalse(battery.needs_service())


class TestTires(unittest.TestCase):
    def test_carrigan_tires_should_be_service(self):
        tire_array = [.90, .91, .92, .93]
        tires = CarriganTires(tire_array)
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_should_not_be_service(self):
        tire_array = [.89, .88, .72, .62]
        tires = CarriganTires(tire_array)
        self.assertFalse(tires.needs_service())

    def test_octoprime_tires_should_be_service(self):
        tire_array = [.99, .99, .99, .99]
        tires = Octoprime(tire_array)
        self.assertTrue(tires.needs_service())

    def test_octoprime_tires_should_not_be_service(self):
        tire_array = [.01, .01, .99, .99]
        tires = Octoprime(tire_array)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()