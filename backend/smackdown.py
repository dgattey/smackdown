import os
import threading
import time
from flask import Flask
import TweetCollecting
import smack_score
import scorekeeping


app = Flask(__name__)

term1="trump"
term2="cruz"

meter = 50.0
smackDict = smack_score.build_dict()

# Starts a basic page, fetching samples
@app.route("/score")
def get_score():
	return str(meter)

@app.route("/history")
def get_history():
    return str(scorekeeping.get_history())

def basicTerms():
    t = threading.Thread(target=getTerms)
    t.daemon = True
    t.start()
    return "Getting tweets for "+term1+", "+term2+"..."

# Simple, calls fetch_samples, should be in a Thread
def getTerms():
    print("Starting fetching...")
    global meter
    while(True):

		term1score = 0.0
		term2score = 0.0
		term1Buf, term2Buf = TweetCollecting.returnBuf()
		for tweet in term1Buf:
			term1score += smack_score.calc_smack_score(tweet, smackDict)

		for tweet in term2Buf:
			term2score += smack_score.calc_smack_score(tweet, smackDict)

		meter = scorekeeping.add_score(term1score, term2score)
		print meter
		time.sleep(5)



if __name__ == "__main__":

    t= threading.Thread(target=TweetCollecting.fetch_samples, args = (term1, term2))
    t.daemon = True
    t.start()
    t1= threading.Thread(target=getTerms)
    t1.daemon = True
    t1.start()

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
