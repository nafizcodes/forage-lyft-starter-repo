import unittest
from datetime import datetime

# Engines
from engine.capulet_engine import Capulet
from engine.willoughby_engine import Willoughby
from engine.sternman_engine import Sternman

# Batteries
from battery.spindler_battery import Spindler
from battery.nubbin_battery import Nubbin


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
    def test_spindler_battery_should_be_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = Spindler(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = Spindler(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    # Nubbin Battery - should be serviced once every 4 years
    def test_nubbin_battery_should_be_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        battery = Nubbin(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_be_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = Nubbin(last_service_date, current_date)
        self.assertTrue(battery.needs_service())


if __name__ == '__main__':
    unittest.main()

'''


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
'''
