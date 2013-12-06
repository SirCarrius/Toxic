Toxic (0.5.0)
=======

Tools for Syndromic Surveillance using Social Media

This version calculates:

1. Semantic distance

TODO:
(How to include all python files in a directory.)
(Explanation of semantic distance.)

Semantic distance
-----------------

The semantic distance aims to quantify how different the meaning of two pieces of text are. Prior approaches considered the number of words in common. This does not account for sentences that use different words but mean the same thing. 

Consider two strings, *A* and *B* each of which have _n_ words. The semantic distance between *A* and *B* is the average semantic distance between all pairs of words from *A* and *B*. The semantic distance between two words is 0 if the words are the same. If the words are different, it is their path similarity on WordNet. Path similarity refers to the shortest path that connects the senses (hypernyms and hyponyms) of the two words. 