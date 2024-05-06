# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:29:59 2024

@author: Allison
"""

def QualifyingPointsUpdate(qualifyingPosition):
    if qualifyingPosition =='1':
        addedValue=10
    elif qualifyingPosition == '2':
        addedValue = 9
    elif qualifyingPosition == '3':
        addedValue = 8
    elif qualifyingPosition == '4':
        addedValue = 7
    elif qualifyingPosition == '5':
        addedValue = 6
    elif qualifyingPosition == '6':
        addedValue = 5
    elif qualifyingPosition == '7':
        addedValue = 4
    elif qualifyingPosition == '8':
        addedValue = 3
    elif qualifyingPosition == '9':
        addedValue = 2
    elif qualifyingPosition == '10':
        addedValue = 1
    elif qualifyingPosition =='disqualified':
        addedValue = -10
    elif qualifyingPosition == 'no time set':
        addedValue = -5
    else:
        addedValue=0
    return(addedValue)