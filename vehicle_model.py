#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Vehicle(object):

    def __init__(self, marca_val, modelo_val, tipo_vehiculo_val):
        self.marca = marca_val
        self.modelo = modelo_val
        self.tipo_vehiculo = tipo_vehiculo_val

    def get_full_vehicle(self):
        return "Marca: {}; Modelo: {}; Tipo de vehículo: {}".format(self.marca, self.modelo, self.tipo_vehiculo)
