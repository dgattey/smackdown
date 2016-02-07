import string
smack_dict = {}
### Input: A string of a tweet, with either #panthers or #broncos
### Output: A "smack" sentiment score for the tweet. More positive = more smack
def calc_smack_score(tweet):

	#Clean words in tweet
	words = tweet.split()
	charsToRemove = string.punctuation
	cleanwords = []
	for word in words:
		cleanword = ''.join([c for c in word if c not in charsToRemove])
		cleanword = cleanword.lower()
		cleanwords.append(cleanword)

	#Calculate total score
	score = 0
	for w in cleanwords:
		if w in smack_dict:
			wordscore = smack_dict[w]
			score += wordscore
	return abs(score)

### Returns a dictionary of words with negative sentiment (smackers)
def build_dict():
	sentiment_file = open('AFINN-111.txt')
	global smack_dict
	for line in sentiment_file:
		if len(line.split())==2:
			word = line.split()[0]
			score = float(line.split()[1])
			if score < 0:
				smack_dict[word] = score
