# -*- coding: utf-8 -*-

import sys
import tweepy
import webbrowser

# Query terms

Q = sys.argv[1:] 
count=1;
fileCount=1;
filename= "dataFile-1.txt"
# Get these values from your application settings.

CONSUMER_KEY = 'PtQ1nInp50HGGpLGemXuXg'
CONSUMER_SECRET = 'd2OeHaOmMiyik4NJ798aSBIVhmE3jXbf9ksyggPgD0'

# Get these values from the "My Access Token" link located in the
# margin of your application details, or perform the full OAuth
# dance.

ACCESS_TOKEN = '65635927-OWtQ7cHurKcyDbbNfKfZ6KfbhSQfcAPXlymTrUkRg'
ACCESS_TOKEN_SECRET = 'CS0d4ADDfbHRoJWYVOnsido3EoYQPoQsG025QqosQ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Note: Had you wanted to perform the full OAuth dance instead of using
# an access key and access secret, you could have uses the following 
# four lines of code instead of the previous line that manually set the
# access token via auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET).
# 
# auth_url = auth.get_authorization_url(signin_with_twitter=True)
# webbrowser.open(auth_url)
# verifier = raw_input('PIN: ').strip()
# auth.get_access_token(verifier)

class StdOutListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream. 
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_status(self, status):
        
        # We'll simply print some values in a tab-delimited format
        # suitable for capturing to a flat file but you could opt 
        # store them elsewhere, retweet select statuses, etc.

        try:
            #print "%s\t%s\t%s\t%s" % (status.text,status.author.screen_name, status.created_at, status.source,)
            updateFile(status.text,status.author.screen_name, status.created_at, status.source,);
        except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            pass

    def on_error(self, status):
        print status


def updateFile(txt,scr_name,created_at,source):
    if(count==1000):
        count=0;
        fileCount= fileCount+1;
        filename="dataFile-"+fileCount+".txt";
    count=count+1;    
    file= open(filename,"a")
    file.write(scr_name+" ::: "+created_at+" ::: "+txt+"\n")
    file.close()

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = tweepy.Stream(auth, l)    
    stream.filter()