#! /usr/bin/env python
# -*- coding: utf-8 -*-
from vehicle_model import Vehicle


class Car(Vehicle):

    def __init__(self, kms_realizados_val, itv_val, *args):
        super(Car, self).__init__(*args)
        self.kms_realizados = kms_realizados_val
        self.itv = itv_val

    def get_full_car(self):
        return "Kms: {}; ITV: {};".format(self.kms_realizados, self.itv)

    def get_atributos(self, indice):
        if indice == 0:
            return self.marca
        elif indice == 1:
            return self.modelo
        elif indice == 2:
            return self.tipo_vehiculo
        elif indice == 3:
            return self.kms_realizados
        elif indice == 4:
            return self.itv
        else:
            return None
