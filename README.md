Toxic (1.0.0)
=======

Tools for Syndromic Surveillance using Social Media


Semantic distance
-----------------

The *semantic distance* quantifies the difference in meaning between two pieces of text. It ranges between 0 and 1. Prior approaches considered the number of words in common. This does not account for sentences that use different words but mean the same thing. 

Consider two strings, *A* and *B* each of which have _n_ words. The semantic distance between *A* and *B* is the average semantic distance between all pairs of words from *A* and *B*. The semantic distance between two words is 0 if the words are the same. If the words are different, it is their path similarity on WordNet. Path similarity refers to the shortest path that connects the senses (hypernyms and hyponyms) of the two words. 

Averaging accounts for length. 

Pitfalls
________________

Some words are not in WordNet. Some meanings of words are not in WordNet. These omissions bias semantic distance towards more established meanings of words, which suggests that the semantic distance is unreliable for texts full of slang or highly metaphorical language. 

Despite these limitations, the semantic distance provides a useful and simple way to quantify meaning. These limitations, moreover, can be overcome by extending WordNet to account for new words or new meanings of words. 