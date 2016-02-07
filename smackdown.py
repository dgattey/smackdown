import os
import threading
import time
from flask import Flask
from flask.ext.cors import CORS, cross_origin
import TweetCollecting
import smack_score
import scorekeeping
import json


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


term1={"term": "panthers", "related":"carolina,newton,cameronnewton,j_no24,norman,beatthepanthers,broncoscountry", "desc": "Carolina Panthers"}
term2={"term": "broncos", "related":"manning,miller,keeppounding,beatthebroncos", "desc": "Denver Broncos"}

# term1={"term": "trump", "related":"donald,realdonaldtrump,makeamercicangreatagain", "desc": "Donald Trump"}
# term2={"term": "cruz", "related":"ted,tedcruz,cruzcrew", "desc": "Ted Cruz"}

# term1={"term": "clinton", "related":"hillary,hillaryclinton" "desc": "Hillary Clinton"}
# term2={"term": "sanders", "related":"bernie,sensanders,berniesanders" "desc": "Bernie Sanders"}



meter = 50.0

# Starts a basic page, fetching samples
@app.route("/score")
@cross_origin()
def get_score():
	return str(meter)

@app.route("/lastTweets")
@cross_origin()
def get_lastTweets():

    return str(TweetCollecting.lastTweets())

@app.route("/history")
@cross_origin()
def get_history():
    return str(scorekeeping.get_history())

@app.route("/info")
@cross_origin()
def get_info():
    return json.dumps({"team1": term1, "team2": term2})

def basicTerms():
    t = threading.Thread(target=getTerms)
    t.daemon = True
    t.start()
    return "Getting tweets for "+term1["term"]+", "+term2["term"]+"..."

# Simple, calls fetch_samples, should be in a Thread
def getTerms():
    print("Starting fetching...")
    global meter
    while(True):

		term1score = 0.0
		term2score = 0.0
		term1Buf, term2Buf = TweetCollecting.returnBuf()
		for tweet in term1Buf:
			term1score += smack_score.calc_smack_score(tweet)

		for tweet in term2Buf:
			term2score += smack_score.calc_smack_score(tweet)

		meter = scorekeeping.add_score(term1score, term2score)
		print meter
		time.sleep(3)



if __name__ == "__main__":
    smack_score.build_dict()

    t= threading.Thread(target=TweetCollecting.fetch_samples, args = (term1["term"], term1["related"], term2["term"], term2["related"]))
    t.daemon = True
    t.start()
    t1= threading.Thread(target=getTerms)
    t1.daemon = True
    t1.start()


    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

