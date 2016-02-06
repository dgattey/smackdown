import os
import threading
from flask import Flask
from TweetCollecting import fetch_samples

app = Flask(__name__)

term1="trump"
term2="beyonce"

# Starts a basic page, fetching samples
@app.route("/")
def basicTerms():
    t = threading.Thread(target=getTerms)
    t.daemon = True
    t.start()
    return "Getting tweets for "+term1+", "+term2+"..."

# Simple, calls fetch_samples, should be in a Thread
def getTerms():
    print("Starting fetching...")
    fetch_samples(term1, term2)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
