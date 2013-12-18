import time,tweepy,sys,json

from Listener import Listener

class Twitter(object):
	def __init__(self,query):
		self.query = query
		self.tokens = json.load(open('./api/tokens.json','rb')) #This is dangerous, need to use better relative paths

		self.consumer_key=self.tokens['twitter']['consumer-key']
		self.consumer_secret=self.tokens['twitter']['consumer-secret']

		self.access_token=self.tokens['twitter']['oauth-token']
		self.access_token_secret=self.tokens['twitter']['oauth-secret']

		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret)

		self.stream = tweepy.Stream(self.auth,Listener('-'.join(self.query)))

		print 'Streaming started...'

		try:
			self.stream.filter(track=self.query)
		except AttributeError as inst:
			print inst
			self.stream.disconnect()
