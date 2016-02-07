#! /usr/bin/python
import sys
import time



# number of tweets, and number of scores. 
num_intervals = 3 	# how many time intervals do we keep data for?
interval = 60 		# start using 1 minute as a time interval
#score_table_a = [[0, 0]]*num_intervals	# each entry in this table is [# of tweets, total score]
# not recording the number of tweets now. Each entry is the total score for that interval
score_table_a = [0]*num_intervals
last_update = 0
score_table_b = [0]*num_intervals	

# history - for as long as the app has been running, it collects data
history = []		# this is an array of tuples


# Input: the new score of the tweet
def add_score(score_a, score_b):
	# check to see if it's been more than an interval since the last update
	# if it's been longer than an interval, need to update the score table
	global last_update
	global score_table_a
	global score_table_b
	now = time.time()
	if now > (last_update + interval):
		last_update = now
		score_table_a = score_table_a[1:]
		score_table_a.append(0)
		score_table_b = score_table_b[1:]
		score_table_b.append(0)
	# now update the current scores
	score_table_a[-1] += score_a
	score_table_b[-1] += score_b
	return score_now(now)


# outputs a number from 0 to 100 that the dial should have
# score is calculated based on data from the last minute.
def score_now(time):
	# create a scale -> 0 is at team a, 100 is at team b
	a = 0
	b = 0
	for i in range(num_intervals):
		a += score_table_a[i]
		b += score_table_b[i]
	a = float(a)
	b = float(b)
	score = ((b/(a+b))*100)
	history.append((time, score))
	return score

