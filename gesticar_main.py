#! /usr/bin/env python
# -*- coding: utf-8 -*-

__autor__='Angel Alvarez'

from vehicle_model import Vehicle
from car_model import Car


def es_numero(num):
    lo_es = None
    try:
        numerete = int(num)
        lo_es = True
    except ValueError:
        lo_es = False
    return lo_es


def es_opcion(opc):
    if opc == 1 or opc == 2 or opc == 3:
        return True
    else:
        return False


def dame_la_opcion(opc):
    opcion = None
    try:
        opcion = int(opc)
    except ValueError:
        opcion = -1
    return opcion


def desea_salir(salir):
    if salir == 's' or salir == 'S':
        return True
    else:
        return False


def muestra_menu():
    print
    print "Seleccione una opción:"
    print "1.-Listar vehículos."
    print "2.-Editar kilómetros y fecha ITV."
    print "3.-Añadir vehículo."
    print "Pulse 'S' para salir."
    print
    return raw_input("¿Que opción desea?: ")


def dame_atributos(indice):
    if indice == 0:
        return "Marca"
    elif indice == 1:
        return "Modelo"
    elif indice == 2:
        return "Kms"
    elif indice == 3:
        return "ITV"
    else:
        return None


def listar_vehiculos(cars):
    for indice, coches in enumerate(cars):
        print "ID: " + str(indice)
        print coches.get_full_vehicle()
        print coches.get_full_car()
        #print coches.itv
        print

    if not cars:
        print "No existen vehículos."


def editar_vehiculos(cars):
    print "Mojon"


def alta_nuevo_coche(cars):
    print "Berbenero"


def saliendo():
    print
    print "Gracias por usar GestiCar Soft."
    raw_input("Cerrando. Pulse cualquier tecla..")


def main():
    car1 = Vehicle(marca_val="VW", modelo_val="Golf IV")
    car2 = Car(53232, 2019, "Seat", "Alhambra")
    car3 = Car(215000, 2019, "VW", "Golf IV")
    car4 = Car(0, 2023, "BMW", "Serie 2 Gran Tourer")
    cochazos = [car2, car3, car4]

    opcion = False #muestra_menu()[0]
    salir = False
    while not salir:#not opcion:#desea_salir(opcion):
        opcion = muestra_menu()[0]
        if es_numero(opcion):
            if es_opcion(dame_la_opcion(opcion)):
                la_opcion = dame_la_opcion(opcion)
                if la_opcion == 1:
                    listar_vehiculos(cochazos)
                elif la_opcion == 2:
                    editar_vehiculos(cochazos)
                elif la_opcion == 3:
                    alta_nuevo_coche(cochazos)
                elif la_opcion == -1:
                    print "Lo siento, la opcion no es validad."
            else:
                print "Seleccione una opcion valida."
        elif desea_salir(opcion):
            saliendo()
            salir = True
        else:
            print "La opción no es correcta."

    #print car.get_full_vehicle()
    #print car2.get_full_car()
    #print "{} {}".format(car2.get_full_vehicle(), car2.get_full_car())


if __name__ == "__main__":
    main()
