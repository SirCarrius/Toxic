ToxRuby
=======

Tools for Toxicovigilance in Ruby (Version 0.5.0)

This version (i) retrieves tweets from Twitter's Streaming API, (ii) uses a Naive Bayesian Classifier 
to filter out interesting messages, and (iii) analyzes characteristics of that substream. In particular, it 
looks at (i) how the relative prominence of this substream varies with geometry and (ii) what identifying 
semantic characteristics that substream has. 

Program Flow (activated by invoking main.sh)
_____________

                |----------Call "ruby **twitter-ruby.rb** -d DRUG -o OUTPUT"
                |                            |
                |                            |-------------------------------------------|
                |                            V                                           V
                |            Search Twitter's Streaming API for DRUG         Search Twitter's Streaming API for NULL
                |             (DRUG is a string of keywords, search is       (Searching for NULL provides a negative
                |             inclusive OR over subsets of those keywords.)   control.)
                |                            |                                           |
                |                            V                                           V
                |                         Each tweet is stored as an element in a JSON array
                |          
                |----------Call "ruby ** NB_classifier_alexandru.rb**"
                |                         |
                |           --------------|-------------------------------------    
                |           |                         |                        |
                |           V                         V                        V
                |        Train                      Test                   Evaluate
                |    _________________________    __________________     ______________
                |    | 0: not about drinking |    |...             |    |Apply to new  |
                |    | 1: about drinking     |    |                |    |data sets     |
                |    | 2: maybe              |    |                |    |              |
                |    |_______________________|    |________________|    |______________|
                |               |                          |                    
                |       ||Curated Data Set||     ||Second Curated Set||
                |
                |     
                |
                V
