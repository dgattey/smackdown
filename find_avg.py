#! /usr/bin/python
import sys


total_a = 0
total_b = 0

# takes in a tweet, and adjusts the overall averages
def overall_avg(score, team):
	if team == 'a':
		total_a += score
	else:
		total_b += score




# takes the raw scores for teams a and b, and outputs the number from 0 to 100 that the dial should have
def normalize(team_a, team_b):
	# create a scale -> 0 is at team a, 100 is at team b
	diff = team_a - team_b
	tot = team_a + team_b
	return (0.5 + (diff/(2*tot)))*100

