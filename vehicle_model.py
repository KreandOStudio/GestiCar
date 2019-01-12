#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Vehicle(object):

    def __init__(self, marca_val, modelo_val):
        self.marca = marca_val
        self.modelo = modelo_val

    def get_full_vehicle(self):
        return "Marca: {}; Modelo: {};".format(self.marca, self.modelo)
