# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 08:44:30 2020

@author: Simon
"""

"""
Author:         Simon Schalk S1910632012
Title:          Schaltjahr
Discription:    Ueberpuefung ob ein beliebiges Jahr ein Schaltjahr ist.
Last Change:    03.01.2020
"""


def Schaltjahr(Jahr):
    #Ueberpruefung mit den angegbenen Parameter ob es ein Schaltjar ist.
    if Jahr % 4 == 0 and Jahr % 400 == 0 or Jahr % 4 == 0 and Jahr % 100 != 0:
        return 'Schaltjahr'
    else:
        return 'Kein Schaltjahr'
