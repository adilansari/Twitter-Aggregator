# -*- coding: utf-8 -*-

import sys
import tweepy
import webbrowser

# Query terms

Q = sys.argv[1:] 

CONSUMER_KEY = ''
CONSUMER_SECRET = ''


ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


f= open("dataFile.txt","a");
class StdOutListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream. 
    This is a basic listener that just prints received tweets to stdout.
    """
    
    def on_status(self, status):
        global f
        try:
            print "%s\t\t%s" % (status.text, status.created_at);            
            #f= open("dataFile-2.txt","a");
            f.write(str(status.text)+"\n");
            #f.close()
            
        except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            f.close
            pass

    def on_error(self, status):
        print status



if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = tweepy.Stream(auth, l, timeout= None)    
    setTerms = ['arsenal']
    #stream.filter(track=Q)
    stream.sample(count=None, async=True)