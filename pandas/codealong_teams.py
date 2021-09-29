# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 17:59:07 2021

@author: BBarsch
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# %matplotlib qt

teams = pd.read_csv('teams.csv')[['yearID', 'franchID', 'name', 'G', 'SO']] 
teams.head()

# PreCompute Data
# Team Level SOG
team_sog = (
    teams
    .query('yearID>=1900')
    .assign(SOG = lambda d: d.SO / d.G)

)
red_sox_sog = (
    team_sog
    .query('name == "Boston Red Sox"')

)

league_sog = (
    team_sog
    .groupby('yearID', as_index=False)
    .agg(SOG = ('SOG', 'mean'))

)
league_sog.head()

# Plot Data
# Plot setup
plt.rcParams['figure.figsize'] = (20,8)
plt.style.use('fivethirtyeight')

# Add a scatter plot layer for all SOGs.
plt.scatter(
    team_sog['yearID'],
    team_sog['SOG'],
#     color = 'lightgray',
    color = 'gray',
    alpha = 0.2
)

# Add a line plot layer for a specific team (Red Sox - orange line)
plt.plot(
 red_sox_sog['yearID'],
    red_sox_sog['SOG'],
    color = 'orange',
    marker = 'o'
  
)

# Add a line plot layer for the entire league (blue line)
plt.plot(
 league_sog['yearID'],
    league_sog['SOG'],
    color = 'steelblue',
    marker = 'o'
  
)

# Change axis limits
plt.ylim(-0.1, 13)
plt.axhline(xmin=0, color='black')

# Add text annotation layer
plt.text(
 1914,
    1,
    s = 'US enters WW1'
)

plt.text(
 1885,
    14,
    s = 'Strikeout on the rise',
    fontsize=24,
    fontweight='bold'
)

plt.text(
 1883,
    13,
    s = 'There were more Strikeout on the rise',
    fontsize=24,
)

# Add title, subtitle, etc
