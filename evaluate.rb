require 'nbayes'
require 'awesome_print'
require 'json'
require 'engtagger'


filename = 'classifier_new.nb'
alcohol = NBayes::Base.from(filename)

tokens = "I am drinking beer right now".split(/\s+/)
result = alcohol.classify(tokens)

filename = "positive-control_.txt"
totalcount = 0
yescount = 0
counter =0

results = Hash.new

def ngrams(n,string)
	return string.split(' ').each_cons(n).to_a
end

to_classify_file = File.readlines("positive-control_.txt")[0].split(',')
to_classify_file.each do |line|
  tokens = line.split(' ')

  unigrams = ngrams(1,line)
  bigrams = ngrams(2,line)
  trigrams = ngrams(3,line)
   
   tgr = EngTagger.new
   pos= tgr.get_readable(line).split(" ")

  rating = alcohol.classify(unigrams | bigrams | trigrams | pos)
  results[line] = rating
end

ap results

File.open('validation-results_.json','w') do |f|
  f.write(results.to_json)
end