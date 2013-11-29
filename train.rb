require 'nbayes'
require 'spreadsheet'
require 'awesome_print'

#returns tweet in array form with stopwords taken out
#takes in the parameters
#tweet:tweet from spreadsheet
#stopwords: stopwords from file "stopwords" 
def createStrippedTweet(tweet,stopwords)
     stripped_tweet = []
     word = tweet.split(/\s+/)
     word.each do |w|
          flag = true
          stopwords.each do |s|
               flag = false if s.chomp == w
          end
          stripped_tweet<<w if flag
     end
     return stripped_tweet   
end

#returns every possible combination of n words in a tweet
#takes in parameters
#tweet: tweet in array form
#n: ngram
def createNgram(tweet,n)
     combi = tweet.combination(n).to_a
     ngram_combo =[]
     combi.each do |i|
          ngram = ""
          i.each do |j|
               ngram = ngram + j
               ngram = ngram +" "
          end
          ngram_combo<<ngram.rstrip
     end
     return ngram_combo
end

alcohol = NBayes::Base.new
stop = File.readlines("stopwords")

rating = {'0' => :no, '1' => :yes, '2' =>:maybe}
#classifiers.txt contains the SUBSTANCE_geo.txt files delimited by |
txtfiles = File.read('classifiers.txt').split(' |')
txtfiles.each do |spread|
     book = Spreadsheet.open spread;
     sheet1 = book.worksheet 0
     sheet1.each do |row|
          if !row[1].nil?
               #taking out stopwords
               clean_tweet = createStrippedTweet(row[0],stop).reject!(&:empty?)
               #creating ngrams
               bigrams = createNgram(clean_tweet,2)
               trigrams = createNgram(clean_tweet,3)
               #the training
               alcohol.train(bigrams | clean_tweet | trigrams,rating[row[1].to_i.to_s])
          end
     end
end

alcohol.dump('classifier_new.nb')