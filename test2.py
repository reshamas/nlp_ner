from nltk.util import ngrams

mytuple = (('s', 'O'), ('p', 'I'), ('a', 'B-men'), ('m', 'B-obj'), \
           ('m', 'O-p'), ('o', 'B-url'), ('r', 'B-oth'), ('e', 'I-other'))


for item in mytuple:
    print item[0], item[1]

tokens = [x[0] for x in mytuple]
tclass = [x[1] for x in mytuple]

print "\ntokens:"
print tokens

n_grams = 5
gramitems = ngrams(tokens, n_grams)
#print len(gramitems)

print "\ntclass: "
print tclass
print "\n"

#for index, item in enumerate(gramitems, start=0):   # default is zero
#        print(index, item)
#        print tclass[index]

import numpy as np
#list(np.array(l).flat)
        
for index, grams in enumerate(gramitems, start=0):
        print "\ngrams:  ", grams
        print "tclass: ", tclass[index]
        #connected = zip(grams)
        #print connected
        
        gramsjoined = "".join(grams)
        #temp = np.array(grams).flat
        print "grams:  ", gramsjoined
        

        
