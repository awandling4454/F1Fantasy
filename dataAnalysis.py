# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:04:42 2024

@author: Allison
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from getPoints import *

fantasyDF=getPoints('fantasy.xlsx')
qualifyingResultsDF = getPoints('qualifyingResults.xlsx')
qualifyingResultsFantasyDF = getPoints('qualifyingResultsFantasy.xlsx')
raceResultsDF = getPoints('raceResults.xlsx')
raceResultsFantasyDF = getPoints('raceResultsFantasy.xlsx')
qualifyingRaceResultsDF = getPoints('qualifyingAndRaceResults.xlsx')
driverOfTheDayDF = getPoints('driverOfTheDay.xlsx')
fastestLapDF = getPoints('fastestLap.xlsx')
leaderPointsDF = getPoints('leaderboard.xlsx')
overtakesDF = getPoints('overtakes.xlsx')


QualifyingRes = (qualifyingResultsDF.iloc[3].apply(int))
print(QualifyingRes)
QualifyingRes.plot.bar()


