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

#with open("data/all.iob", "r") as infile:
#with open("data/lines350.iob", "r") as infile:
#with open("data/lines60.iob", "r") as infile:
with open("data/lines50.iob", "r") as infile:
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
#d = defaultdict(list)
d = multi_key_dict()

# Fill in the entries one by one
#d["age"] = 25
for line in ner_list:
    setkey = tuple((line[0], line[1], line[2], line[4], line[5]))
    #print setkey
    d[setkey].append(line[3])
    

print "len(d): ", len(d)

#for i in d:
#        print i, d[i]
        
#for k, v in d.iteritems():
#        print k, v

#print sorted(d, key=lambda key: d[key])

from pprint import pprint

pprint (sorted(d.items()))


print "------------------------------"
i = 1

#for item in ner_list[:50]:
    #tweetnum = item
    #print item
    #print item[1]
    #print item

print "------------------------------"


#for tweet in tweetlist:





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
