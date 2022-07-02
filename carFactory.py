# Engines
from engine.capulet_engine import Capulet
from engine.willoughby_engine import Willoughby
from engine.sternman_engine import Sternman

# Batteries
from battery.spindler_battery import Spindler
from battery.nubbin_battery import Nubbin

# Car
from car.car import Car


class CarFactory:
    # Calliope - Capulet Engine, Spindler Battery
    def Calliope(self, last_service_mileage, current_mileage, last_service_date, current_date):
        engine = Capulet(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    # Glissade - Willoughby Engine, Spindler Battery


def Glissade(self, last_service_mileage, current_mileage, last_service_date, current_date):
    engine = Willoughby(last_service_mileage, current_mileage)
    battery = Spindler(last_service_date, current_date)
    car = Car(engine, battery)
    return car

    # Palindrome - Sternman Engine, Spindler Battery


def Palindrome(self, warning_light_on, last_service_date, current_date):
    engine = Sternman(warning_light_on)
    battery = Spindler(last_service_date, current_date)
    car = Car(engine, battery)
    return car

    # Rorschach - Willoughby Engine, Nubbin Battery


def Rorschach(self, last_service_mileage, current_mileage, last_service_date, current_date):
    engine = Willoughby(last_service_mileage, current_mileage)
    battery = Nubbin(last_service_date, current_date)
    car = Car(engine, battery)
    return car

    # Thovex - Capulet Engine, Nubbin Battery


def Thovex(self, last_service_mileage, current_mileage, last_service_date, current_date):
    engine = Capulet(last_service_mileage, current_mileage)
    battery = Nubbin(last_service_date, current_date)
    car = Car(engine, battery)
    return car
