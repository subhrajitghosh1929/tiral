# MassConversion.py
"""Conversion functions between different masses"""

#Constants
KG_TO_TONNE = 0.001
TONNE_TO_KG = 1 / KG_TO_TONNE
KG_TO_POUND = 2.20462
POUND_TO_KG = 1 / KG_TO_POUND

#Functions
def kgtotonne(kg):
    """Returns: kilogram converted to tonnes"""
    return kg * KG_TO_TONNE
print(kgtotonne)
def tonnetokg(tonne):
    """Returns: tonne converted to kilogram"""
    return tonne * TONNE_TO_KG
print(tonnetokg)
def kgtopound(kg):
    """Returns: kilogram converted to pound"""
    return kg * KG_TO_POUND
print(kgtopound)
def poundtokg(pound):
    """Returns: pound converted to kilogram"""
    return pound * POUND_TO_KG
print(poundtokg)
