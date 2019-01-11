#! /usr/bin/env python
# -*- coding: utf-8 -*-

from vehicle_model import Vehicle
from car_model import Car


def main():
    car = Vehicle(marca_val="VW", modelo_val="Golf IV")
    car2 = Car(53232, 2019, "Seat", "Alhambra")
    print car.get_full_vehicle()
    print car2.get_full_car()
    print "{} {}".format(car2.get_full_vehicle(), car2.get_full_car())


if __name__ == "__main__":
    main()
