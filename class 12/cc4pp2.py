# lengthconversion.py
"""Conversion functions for various lengths"""

#Constants
MILE_TO_KM = 1.609344
KM_TO_MILE = 1 / MILE_TO_KM
FEET_TO_INCHES = 12
INCHES_TO_FEET = 1 / FEET_TO_INCHES

#Functions
def miletokm(miles):
    """Returns: miles converted to kilometers"""
    return miles * MILE_TO_KM

def kmtomile(kilometers):
    """Returns: kilometers converted to miles"""
    return kilometers * KM_TO_MILE

def feettoinches(feet):
    """Returns: feet converted to inches"""
    return feet * FEET_TO_INCHES

def inchestofeet(inches):
    """Returns: inches converted to feet"""
    return inches * INCHES_TO_FEET
