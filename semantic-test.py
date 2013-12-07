from SemanticString import SemanticString
from nltk.corpus import wordnet

test_string = "This is very good."
other_string = "This is slightly bad."

#Drop down to testing Semantic Word
d1 = SemanticString(test_string)
d2 = SemanticString(other_string)

print d1-d2