#! /usr/bin/python
import sys
import time



# number of tweets, and number of scores. 
num_intervals = 3 	# how many time intervals do we keep data for?
interval = 60 		# start using 1 minute as a time interval
score_table_a = [[0, 0]]*num_intervals	# each entry in this table is [# of tweets, total score]
last_update = 0
score_table_b = [[0, 0]]*num_intervals	


# Input: the new score of the tweet
# the team that is doing the smacking. - CHECK THIS
def add_score(score, team):
	# check to see if it's been more than an interval since the last update
	# if it's been longer than an interval, need to update the score table
	global last_update
	global score_table_a
	global score_table_b
	if time.time() > (last_update + interval):
		last_update = time.time()
		score_table_a = score_table_a[1:]
		score_table_a.append([0, 0])
		score_table_b = score_table_b[1:]
		score_table_b.append([0, 0])
	# now update the current scores
	if team == 'a':
		score_table_a[-1][0] += 1
		score_table_a[-1][1] += score
	if team == 'b':
		score_table_b[-1][0] += 1
		score_table_b[-1][1] += score
	#print score_table_a
	#print score_table_b


# outputs a number from 0 to 100 that the dial should have
# score is calculated based on data from the last minute.
def score_now():
	# create a scale -> 0 is at team a, 100 is at team b
	a = team_a[-1][1]
	b = team_b[-1][1]
	diff = team_a - team_b
	tot = team_a + team_b
	return (0.5 + (diff/(2*tot)))*100



"""
# takes the raw scores for teams a and b, 
# outputs the number from 0 to 100 that the dial should have
def normalize(team_a, team_b):
	# create a scale -> 0 is at team a, 100 is at team b
	diff = team_a - team_b
	tot = team_a + team_b
	return (0.5 + (diff/(2*tot)))*100
"""

