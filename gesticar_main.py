#! /usr/bin/env python
# -*- coding: utf-8 -*-

__autor__='Angel Alvarez'

from vehicle_model import Vehicle
from car_model import Car


def saliendo():
    print
    print "Gracias por usar GestiCar Soft."
    raw_input("Cerrando. Pulse cualquier tecla..")


def desea_salir(salir):
    if salir == 's' or salir == 'S':
        return True
    else:
        return False


def es_opcion(opc):
    if opc == 1 or opc == 2 or opc == 3:
        return True
    else:
        return False


def es_numero(num):
    lo_es = None
    try:
        numerete = int(num)
        lo_es = True
    except ValueError:
        lo_es = False
    return lo_es


def dame_el_numero(opc):
    opcion = None
    try:
        opcion = int(opc)
    except ValueError:
        opcion = -1
    return opcion


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
        print

    if not cars:
        print "No existen vehículos."


def editar_vehiculos(cars):
    listar_vehiculos(cars)
    es_todo_correcto = False

    while not es_todo_correcto:
        edit_opcion = raw_input("Seleccione el vehiculo: ")
        if es_numero(edit_opcion):
            if not dame_el_numero(edit_opcion) >= len(cars):
                vehiculo_seleccionado = cars[dame_el_numero(edit_opcion)]
                es_todo_correcto = True
            else:
                print "No ha seleccionado correctamente un vehiculo."
        else:
            print "No es correcto."

    es_todo_correcto = False
    print
    print "Vehiculo seleccionado: {}".format(vehiculo_seleccionado.get_full_vehicle())
    while not es_todo_correcto:
        actualizar_kms = raw_input("Introduzca los kilometros del vehiculo: ")
        if es_numero(actualizar_kms):
            vehiculo_seleccionado.kms_realizados = actualizar_kms
            es_todo_correcto = True
        else:
            print "Error al introducir los datos."

    es_todo_correcto = False
    while not es_todo_correcto:
        actualizar_ITV = raw_input("Introduzca la proxima revision tecnica (ITV): ")
        if es_numero(actualizar_ITV):
            vehiculo_seleccionado.itv = actualizar_ITV
            es_todo_correcto = True
        else:
            print "Error al introducir los datos."

    print
    print "Kilometros e ITV actualizados."


def alta_nuevo_coche(cars):
    print "Añadir un vehiculo: "
    n_marca = raw_input("Introduzca la marca del vehiculo: ")
    n_modelo = raw_input("Introduzca el modelo del vehiculo: ")
    n_kms = 0
    todo_correcto = False
    while not todo_correcto:
        n_itv = raw_input("Introduzca el año de compra del vehiculo: ")
        if es_numero(n_itv):
            itv = dame_el_numero(n_itv) + 4
            todo_correcto = True
        else:
            print "El año no es correcto."

    nuevo_vehiculo = Car(n_kms, itv, n_marca, n_modelo)

    cars.append(nuevo_vehiculo)
    print "Añadido nuevo vehiculo."


def main():
    car2 = Car(53232, 2019, "Seat", "Alhambra")
    car3 = Car(215000, 2019, "VW", "Golf IV")
    car4 = Car(0, 2023, "BMW", "Serie 2 Gran Tourer")
    cochazos = [car2, car3, car4]

    opcion = False
    salir = False
    while not salir:
        opcion = muestra_menu()[0]
        if es_numero(opcion):
            if es_opcion(dame_el_numero(opcion)):
                la_opcion = dame_el_numero(opcion)
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


if __name__ == "__main__":
    main()
