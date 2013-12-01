require 'rubygems'
require 'rwordnet'

lex = WordNet::Lexicon.new

to_classify_file = File.readlines("positive-control_.txt")[0].split(',')
