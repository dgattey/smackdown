import os
import threading
from flask import Flask
from TweetCollecting import fetch_samples
import smack_score
import scorekeeping

# app = Flask(__name__)

term1="trump"
term2="beyonce"
term1score = 0.0
term2score = 0.0
meter = 50.0
smackDict = smack_score.build_dict()

# Starts a basic page, fetching samples
# @app.route("/")
def basicTerms():
    t = threading.Thread(target=getTerms)
    t.daemon = True
    t.start()
    return "Getting tweets for "+term1+", "+term2+"..."

# Simple, calls fetch_samples, should be in a Thread
def getTerms():
    print("Starting fetching...")
    global term1score, term2score
    
    while(True):
	    term1Buf, term2Buf = fetch_samples(term1, term2)
	    for tweet in term1Buf:
	    	term1score += smack_score.calc_smack_score(tweet, smackDict)

	    for tweet in term2Buf:
	    	term2score += smack_score.calc_smack_score(tweet, smackDict)

	    meter = scorekeeping.add_score(term1score, term2score)
	    print meter



if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)

    getTerms()
