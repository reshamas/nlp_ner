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
                    tclass2 = "O-mention"
                    item.append(tclass2) 
                    #print '------'
                    #print item
                    #print tclass2
                
                # Add a class for emojis
                if len(token) > 1 and token[0] == ":":
                    tclass3 = "O-emoji"
                    item.append(tclass3)
                    #print item, tclass1, tclass3
            
                # Add a class for url links
                if token.startswith("http"):
                    tclass4 = "O-url"
                    item.append(tclass4)
                    #print item, tclass1, tclass4

                ner_list.append(item)



print "------------------------------"

print "len(ner_list):  ",  len(ner_list)


print "------------------------------"
for item in ner_list[:50]:
    print item


print "------------------------------"




def ngram(numg, logp):
    for i in range (2,3):
        for tweetnum in range(1,3):
            
    return
    






ngram(4, 1)
