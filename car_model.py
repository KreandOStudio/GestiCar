#! /usr/bin/env python
# -*- coding: utf-8 -*-
from vehicle_model import Vehicle


class Car(Vehicle):

    def __init__(self, kms_realizados_val, itv_val, *args):
        super(Car, self).__init__(*args)
        self.kms_realizados = kms_realizados_val
        self.itv = itv_val

    def get_full_car(self):
        return "|| Kms: {} || ITV: {}".format(self.kms_realizados, self.itv)
