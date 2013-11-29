require 'nbayes'
require 'awesome_print'
require 'json'

filename = 'classifier.nb'
alcohol = NBayes::Base.from(filename)

tokens = "I am drinking beer right now".split(/\s+/)
result = alcohol.classify(tokens)

filename = "positive-control_.txt"
totalcount = 0
yescount = 0
counter =0

results = Hash.new

to_classify_file = File.readlines("positive-control_.txt")[0].split(',')
to_classify_file.each do |line|
  tokens = line.split(' ')
  rating = alcohol.classify(tokens)
  results[line] = rating
end

ap results

File.open('validation-results.json','w') do |f|
  f.write(results.to_json)
end