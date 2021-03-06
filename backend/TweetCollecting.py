# Use: python TweetCollecting.py -term1 coldplay -term2 beyonce

import string
import argparse
import oauth2 as oauth
import urllib2 as urllib
import json
import sys
import csv
import smack_score

# See Assignment 1 instructions for how to get these credentials
access_token_key = "860765546-2UbcgzBroe1J89vv76uC6Afjxz0gxvaaEGAWqFfU"
access_token_secret = "4N7AEzxopWVovxjOWAOnM8tSwy3RwJqNClEpNKeKqr45X"

consumer_key = "rH3Hn1bDwb0DDh4O1mroKhNlZ"
consumer_secret = "zLixgX8qCF1gJ5aEANXkYIURQARkxqEGV1RsmdVhVlX3c6OC30"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response

term1buf = []
term2buf = []
last20 = []
i = 0

def fetch_samples(term1, term1related, term2, term2related):
    url = "https://stream.twitter.com/1.1/statuses/sample.json?language=en"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    term1related = term1related.split(',')
    term2related = term2related.split(',')
    term1related.append(term1)
    term2related.append(term2)
    global last20
    print term1related, term2related
    for line in response:
        line = json.loads(line)
        orline = line['text'].encode('utf-8')
        line = line['text'].encode('utf-8').strip().lower()
        charsToRemove = string.punctuation
        line = ''.join(ch for ch in line if ch not in charsToRemove)
        used = False
        global i
        i += 1
        if i%2 == 0:
            for t1 in term1related:
                if t1 in line and used == False:
                    term1buf.append(line)
                    if len(orline) > 0:
                        last20.append(orline)
                        last20 = last20[-20:]
                    used = True 

            for t2 in term2related:
                if t2 in line and used == False:
                    term2buf.append(line)
                    if len(orline) > 0:
                        last20.append(orline)
                        last20 = last20[-20:]
                    used = True
        else:
            for t2 in term2related:
                if t2 in line and used == False:
                    term2buf.append(line)
                    if len(orline) > 0:
                        last20.append(orline)
                        last20 = last20[-20:]

                    used = True
            for t1 in term1related:
                if t1 in line and used == False:
                    term1buf.append(line)
                    if len(orline) > 0:
                        last20.append(orline)
                        last20 = last20[-20:]
                    used = True 

                                

        
def returnBuf():
    global term1buf 
    global term2buf 

    toReturn = (term1buf, term2buf)
    print toReturn

    term2buf = []
    term1buf = []
    return toReturn

def lastTweets():
    posTweets = []
    for tweet in last20:
        if smack_score.calc_smack_score(tweet) > 0:
            posTweets.append(tweet)
    j = json.dumps(posTweets) 
    return j


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-term1', help='Enter the first term')
    parser.add_argument('-term2', help='Enter the second term')
    opts = parser.parse_args()
    
    fetch_samples(opts.term1, opts.term2)

