from nltk.util import ngrams
import numpy as np

mytuple = (('s', 'O'), ('p', 'I'), ('a', 'B-men'), ('m', 'B-obj'), \
           ('m', 'O-p'), ('o', 'B-url'), ('r', 'B-oth'), ('e', 'I-other'))

#for item in mytuple:
#    print item[0], item[1]

tokens = [x[0] for x in mytuple]
tclass = [x[1] for x in mytuple]

print "\ntokens:"
print tokens

print "\ntclass: "
print tclass



n_grams = 5
max_grams=len(tokens)
print "\nmax_grams:"
print max_grams
gramitems = ngrams(tokens, n_grams)

for index, grams in enumerate(gramitems, start=0):
        print "\ngrams:  ", grams
        print "tclass: ", tclass[index]
                
        gramsjoined = "".join(grams)
        print "grams:  ", gramsjoined
        

        
