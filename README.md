## Install tweepy

The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:
    
	pip install tweepy

You may also use Git to clone the repository from
Github and install it manually:

	git clone https://github.com/tweepy/tweepy.git
	python setup.py install

**Note** only Python 2.5 to 2.7 is supported at
the moment. The Python 3 family is not yet supported.

## Connecting to twitter API

Create your app on [dev.twitter.com/apps](https://dev.twitter.com/apps) and get the corresponding authentication keys.

Since twitter provides several resources to fetch public tweets you can either opt to filter the stream:

	[POST statuses/filter](https://dev.twitter.com/docs/api/1.1/post/statuses/filter)

Or get the sample stream i.e. access only to 1% of the public stream:

	[GET statuses/sample](https://dev.twitter.com/docs/api/1.1/get/statuses/sample)

Documentation
-------------
  - [Website (Work in-progress)](http://tweepy.github.com/)
  - [Twitter Developers](http://dev.twitter.com/)
  - [Python Package Documentation](http://packages.python.org/tweepy/html/index.html)

Community
---------
  - [Google Group/Mailing list](http://groups.google.com/group/tweepy)
  - IRC Chat (Freenode.net #tweepy)
