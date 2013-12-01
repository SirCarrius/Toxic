require 'rubygems'
require 'wordnet'
require 'awesome_print'


tweets = File.readlines("positive-control_.txt")[0].split(',')

corpus_size = tweets.size


(1..corpus_size).each do |i|
	(1..corpus_size).each do |j|
		one = tweets[i].split(" ").map(&:strip)
		two = tweets[j].split(" ").map(&:strip)
		
		
	end
end


tweets.each do |tweet|
	tokens = tweet.split(' ')
end