import tweepy,json,sys,time

from tweepy.streaming import StreamListener
from tweepy import Stream

class Listener(StreamListener):

	def __init__(self,filename, ceiling=400):
		self.ceiling = ceiling
		self.trigger = filename
		super(Listener,self).__init__()

		self.filename = '../data/%s-%s.json'%(filename,time.strftime('%Y%m%d-%H%M%S'))
		self.output = open(self.filename,'wb')
		self.output.write('[')
		self.delout = open('delete.txt','a')
		self.counter = 0

	def __nonzero__(self):
		return self.count > self.ceiling

	def on_data(self, data):
		if  'in_reply_to_status' in data:
			if self.counter < self.ceiling:
				self.on_status(data)
			else:
				self.output.write(']')
				self.output.close()
				return False
		elif 'delete' in data:
			delete = json.loads(data)['delete']['status']
			if self.on_delete(delete['id'], delete['user_id']) is False:
				return False
		elif 'limit' in data:
			if self.on_limit(json.loads(data)['limit']['track']) is False:
				return False
		elif 'warning' in data:
			warning = json.loads(data)['warnings']
			print warning['message']
			return false

	def on_status(self, status):
		self.counter += 1
		if self.counter%400 ==0:
			self.output.write(status)	
			self.output.write(']')
			self.output.close()
			self.output = open('../data/%s-%s.json'%(self.trigger,time.strftime('%Y%m%d-%H%M%S')), 'w')
			self.output.write('[')
		else:
			self.output.write(status + ",")	
		return

	def on_delete(self, status_id, user_id):
		self.delout.write( str(status_id) + "\n")
		return

	def on_limit(self, track):
		sys.stderr.write(str(track) + "\n")
		return

	def on_error(self, status_code):
		sys.stderr.write('Error: ' + str(status_code) + "\n")
		return False

	def on_timeout(self):
		sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
		time.sleep(60)
		return 