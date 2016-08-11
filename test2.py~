from nltk.util import ngrams
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 6
sixgrams = ngrams(sentence, n)
#for grams in sixgrams:
#      print grams

'''
mytuple = ('s', 'p', 'a', 'm', 'm', 'o', 'r', 'e')
myclass = ('O', 'I', 'B-men','B-Obj', 'O-p', 'B-url', 'B-oth','I-other')
print zip(mytuple, myclass)

twograms = ngrams(mytuple, 3)
for grams in twograms:
    print grams
'''

mytuple = (('s', 'O'), ('p', 'I'), ('a', 'B-men'), ('m', 'B-obj'), \
           ('m', 'O-p'), ('o', 'B-url'), ('r', 'B-oth'), ('e', 'I-other'))
#myclass = ('O', 'I', 'Obj', 'O-p')
#print zip(mytuple, myclass)


for item in mytuple:
    print item[0], item[1]

tokens = [x[0] for x in mytuple]
tclass = [x[1] for x in mytuple]

print "tokens:"
print tokens
threegrams = ngrams(tokens, 3)
#print len(threegrams)

print "tclass: "
print tclass
for grams in threegrams:
        print grams
        connected = zip(grams)
        print connected

        
