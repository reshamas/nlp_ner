#------------------------------------------------------------------------------
# Description:   
# Project:       NLP - NER
# Date Updated:  07/28/2016
# Author:
# Updated By:    Reshama
#
# Input:         data/all.iob
# Output:        
# -----------------------------------------------------------------------------
# ner_list:  tweet_num, tweet_item, token, class
# want to add:  tweet_char
# -----------------------------------------------------------------------------
from nltk.util import ngrams

#with open("data/all.iob", "r") as infile:
#with open("data/lines350.iob", "r") as infile:
#with open("data/lines60.iob", "r") as infile:
#with open("data/lines50.iob", "r") as infile:
with open("../data/lines25.iob", "r") as infile:
    ner_list = []
    tweet_num = 1
    tweet_item = 0
    for line in infile:
        line=line.rstrip()
        lineitems = line.split("\t")
        #print lineitems
        if line == '':
            tweet_num += 1
            tweet_item = 0
        else:
            tweet_item += 1
            token = lineitems[0]
            tclass1 = lineitems[1]

            
            #print token, tclass1
            for char in token:
                #print tweet_num, tweet_item, token, char, tclass1
                
                item = [tweet_num, tweet_item, token, char, tclass1]
            
                # add a class for twitter mentions
                if token[0] == "@":
                    tclass2 = "B-mention"
                    #item.append(tclass2)
                    #print '------'
                    #print item
                    #print tclass2
                
                # Add a class for emojis
                elif len(token) > 1 and token[0] == ":":
                    tclass2 = "B-emoji"
                    #item.append(tclass3)
                    #print item, tclass1, tclass3
            
                # Add a class for url links
                elif token.startswith("http"):
                    tclass2 = "B-url"
                    #item.append(tclass4)
                    #print item, tclass1, tclass4

                else:
                    tclass2 = tclass1
                item.append(tclass2)
                ner_list.append(item)



print "------------------------------"

print "len(ner_list):  ",  len(ner_list)

from collections import defaultdict

from multi_key_dict import multi_key_dict


# Empty dict
#d = {}
d = defaultdict(list)
dtweet = defaultdict(list)
dtweetcl = defaultdict(list)
dclass = defaultdict(list)
#d = multi_key_dict()

# Fill in the entries one by one

for line in ner_list:
    print "line: "
    print line
    #setkey = tuple((line[0], line[1], line[2], line[4], line[5]))
    #setkey = tuple(str(line[0]))
    setkey = tuple((line[0], line[1]))
    token = line[3]
    tclass1 = tuple((line[4], line[5]))
    #token_class = tuple((token, line[4], line[5]))
    token_class = list((token, line[4], line[5]))

    #print setkey, token_class
    d[setkey].append(line[3])
    dclass[setkey].append(tclass1)

    dtweet[str(line[0])].append(line[3])
    dtweetcl[str(line[0])].append(line[4])
    
    
#print "\nlen(d=dictionary): ", len(d)
#print "\nlen(dclass dict):  ", len(dclass)

print "\nlen(dtweet dict):  ", len(dtweet)
print "\nlen(dclass dict):  ", len(dtweetcl)

#for i in d:
#        print i, d[i]
        
#for k, v in d.iteritems():
#        print k, v

#print "\nsorted d by key"
#print sorted(d, key=lambda key: d[key])

#from pprint import pprint
#print "\n"
#pprint (sorted(d.items()))

def printDict(dictname):
    for k, v in dictname.items():
        print k, v


print "------------------------------"
print "dict(dtweet): "
printDict(dtweet)
print "------------------------------"
print "dict(dtweetcl): "
printDict(dtweetcl)

print "------------------------------"
# tkey = tweet number 
# tvalue = each character of tweet
# ckey = tweet number
# cvalue = class

from itertools import izip
for (tkey, tvalue), (ckey, cvalue) in izip(dtweet.iteritems(), dtweetcl.iteritems()):
       tweet_length = sum(1 for v in tvalue if v)
       print "\ntweet_length: ", tweet_length
       print tkey
       print tvalue
       print ckey
       print cvalue
       for gramlength in range(3, tweet_length):
           gramitems = ngrams(tvalue, gramlength)

           for index, grams in enumerate(gramitems, start=0):
               #print "\ngrams: ", grams
               #print "\tclass: ", cvalue[index]

               gramsjoined = "".join(grams)
               #print "grams: ", gramsjoined
               
           


'''
print "------------------------------"

for key, value in d.items():
    item_length = sum(1 for v in value if v)
    print "\nitem_length: ", item_length
    #tokens = [x[0] for x in value]
    #tclass = [x[1] for x in value]
    print "key:      ", key   #, value
    print "value:   ", d[key]
    #print d[key][0][1]
    #print d[key[0][0]]
    #print "value[1]: ", value[1]
    #for val in value:
    #    print val
        #print val[1]
        #print type(val)
    #x, y  = d[key]
    #d[key] = x, newy, z

from itertools import izip
for (key, value), (i, j) in izip(d.iteritems(), dclass.iteritems()):
       #print key, value, i, j
       item_length = sum(1 for v in value if v)
       print "\nitem_length: ", item_length
       print key
       print value
       print i
       print j
       #tokens = [x[0] for x in value]      
       #print tokens



           
# prints first part of tuple key
for val in (x[0] for x in d):
        print val

# prints second part of tuple key
for val in (x[1] for x in d):
        print val
'''



'''
#for key, (tokenc, tclass1, tclass2) in d.iteritems():
#    print key
    #print key, tokenc, tclass1
    
i = 1

#for item in ner_list[:50]:
    #tweetnum = item
    #print item
    #print item[1]
    #print item

print "------------------------------"


#maxgrams = len(tweet)


def find_ngrams(input_list, n):
      return zip(*[input_list[i:] for i in range(n)])
  

#test = find_ngrams(ner_list, 3)
#print test
    
def ngram(numg, logp):
    #for i in range (2,3):
    #    for tweetnum in range(1,3):
            
    return


#ngram(4, 1)
'''
