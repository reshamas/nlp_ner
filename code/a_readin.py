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
# include libraries
from nltk.util import ngrams
from collections import defaultdict

# use data (some small subsets to test code)
#with open("../data/all.iob", "r") as infile:
#with open("../data/lines350.iob", "r") as infile:
#with open("../data/lines60.iob", "r") as infile:
#with open("../data/lines50.iob", "r") as infile:

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

# Empty dict
d = defaultdict(list)
dtweet = defaultdict(list)
dtweetcl = defaultdict(list)
dclass = defaultdict(list)

# Fill in the entries one by one

for line in ner_list:
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


def printDict(dictname):
    for k, v in dictname.items():
        print k, v


print "------------------------------"
printDict(dtweet)
print "------------------------------"
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
               
       print "\nmaximum-length gram: "
       print gramsjoined
       print cvalue[index]
