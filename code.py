# --------------
# Using Numpy
print('Using Numpy')
import numpy as np

# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
data_ipl = np.genfromtxt(path, delimiter=',',dtype='str' ,skip_header=True)

# How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind.
print('How many matches were held in total',len(set(data_ipl[:,0])))

# this exercise deals with you getting to know that which are all those six teams that played in the tournament.
team_1 = set(data_ipl[:,3])
team_2 = set(data_ipl[:,4])
print('six teams',team_1.union(team_2))

# An exercise to make you familiar with indexing and slicing up within data.
print('sum of all extras in all deliveries in all matches in the dataset',data_ipl[:,17].astype(float).sum())
print('Total number of exta',len(data_ipl[data_ipl[:,17].astype(float)>0]))

# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
given_batsman = 'ST Jayasuriya'
out_deliveries = data_ipl[data_ipl[:,-3]==given_batsman][:,[11,-2]]
print('array of all delivery numbers when a given player got out',out_deliveries)

# this exercise will help you get the statistics on one particular team
given_team = 'Mumbai Indians'
print('matches the team Mumbai Indians has won the toss',len(set(data_ipl[data_ipl[:,5]==given_team][:,0])))

# An exercise to know who is the most aggresive player or maybe the scoring player 
records_with_six_runs = data_ipl[data_ipl[:,-7].astype(int)==6]
from collections import Counter
sixes_scorers_count = Counter(records_with_six_runs[:,-10])
print('who has scored the maximum no. of sixes overall')
print(max(sixes_scorers_count,key=sixes_scorers_count.get))



print('Using Pandas')

# Using Pandas

# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
import pandas as pd
df = pd.read_csv(path)


# How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind.
print('How many matches were held in total',len(df['match_code'].unique()))

# this exercise deals with you getting to know that which are all those six teams that played in the tournament.
teams = df['team1'].append(df['team2']).unique()
print('six teams',teams)

# An exercise to make you familiar with indexing and slicing up within data.
print('sum of all extras in all deliveries in all matches in the dataset',sum(df['extras']))

# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
given_batsman = 'ST Jayasuriya'
out_deliveries = df[df['player_out']==given_batsman][['inning','delivery','wicket_kind']]
print('array of all delivery numbers when a given player got out',out_deliveries)

# this exercise will help you get the statistics on one particular team
print('matches the team Mumbai Indians has won the toss',len(df[df['toss_winner']=='Mumbai Indians']['match_code'].unique()))

# An exercise to know who is the most aggresive player or maybe the scoring player 
records_with_six_runs = df[df['runs']==6]
sixes_scorers_count = records_with_six_runs['batsman'].value_counts()
print('who has scored the maximum no. of sixes overall')
print(sixes_scorers_count[sixes_scorers_count==sixes_scorers_count.max()])






