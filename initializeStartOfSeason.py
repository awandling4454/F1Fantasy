# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:10:27 2024

@author: Allison
"""

import pandas as pd

driverNames = ['Max Verstappen','Charles Leclerc','Sergio Perez','Carlos Sainz','Oscar Piastri',
               'Lando Norris','George Russel','Fernando Alonso', 'Lance Stroll',
               'Lewis Hamilton','Yuki Tsunoda', 'Oliver Bearman', 'Nico Hulkenberg','Kevin Magnussen',
               'Alexander Albon','Zhou Guanyu','Daniel Ricciardo','Esteban Ocon','Pierre Gasly','Valtteri Bottas','Logan Seargant']
points = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


df_names = pd.DataFrame({'Name':driverNames, 'Initial':points})
print(df_names)
#qualifying Results only
df_names.to_excel('qualifyingResults.xlsx',index = 'False')

#qualifying Results with fantasy points
df_names.to_excel('qualifyingResultsFantasy.xlsx',index='False')

#race results only
df_names.to_excel('raceResults.xlsx', index='False')

#race results fantasy only
df_names.to_excel('raceResultsFantasy.xlsx', index = 'False')

#qualifying and race results
df_names.to_excel('qualifyingAndRaceResults.xlsx', index = 'False')

#driver of the Day
df_names.to_excel('driverOfTheDay.xlsx', index = 'False')

#fastest lap
df_names.to_excel('fastestLap.xlsx', index='False')

#all results
df_names.to_excel('fantasy.xlsx',index = 'False')

#LeaderboardPoints
df_names.to_excel('leaderboard.xlsx',index='False')

#overtakes
df_names.to_excel('overtakes.xlsx', index='False')



print('done')

