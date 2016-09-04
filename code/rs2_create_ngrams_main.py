#------------------------------------------------------------------------------
# Description:   
# Project:       NLP - NER
# Date Updated:  08/25/2016
# Author:        Reshama
# Updated By:    Reshama
# Python:        version 2.7
# Input:         data/all.iob
# Output:        
# -----------------------------------------------------------------------------
# ner_list:  tweet_num, tweet_item, token, class
# want to add:  tweet_char
# -----------------------------------------------------------------------------
# include libraries
from nltk.util import ngrams
from collections import defaultdict
from pprint import pprint
from itertools import izip

# this is sample of raw data structure:
'''
RT    O
@PeterRabbitt    O
:    O
HAPPY    O
BIRTHDAY    O
TO    O
@DaDaDaphne    O
WISHIN    O
'''


def read_data(datafile, logp):
    """
    read in text file and return list with tweet number word number, token and class
    """
    with open(datafile, "r") as infile:
        ner_list = []
        ner_word_list = []
        tweet_num = 1
        tweet_word = 0
        tweet_item = 0
        for line in infile:
            # add a blank line at begining of file, so first tweet follows format
            # tweets are separated by a blank line
            #if tweet_num ==1 and tweet_word ==0:
            #    linetemp = "\n" + line
            #    line = linetemp
            
            # remove carriage return at end of line
            line=line.rstrip()

            # split line items that are separated by tab
            lineitems = line.split("\t")

            # if line is a space, indicates start of new tweet
            # increment tweet number count; reset tweet word count
            if line == '':
                tweet_num += 1
                tweet_word = 0
            else:
                tweet_word += 1
                token = lineitems[0]
                tclass1 = lineitems[1]

                # break each word by each character
                for char in token:
                    # create array with tweet key (num, word) and token, class
                    item = [tweet_num, tweet_word, token, char, tclass1]
                    ner_list.append(item)
            #print tweet_num, tweet_word, token, tclass1
            item_word_list = [tweet_num, tweet_word, token, tclass1]
            ner_word_list.append(item_word_list)
        if logp == 1:
            print 'ner_list: '
            print 'len(ner_list): ', len(ner_list)
            pprint(ner_list[0:10])
            print '\nner_word_list: '
            print 'len(ner_word_list): ', len(ner_word_list)
            pprint(ner_word_list[0:10])
        return ner_list, ner_word_list
    
# this is the full data
#ner_list = read_data("../data/all.iob", 0)

# this is what ner_list looks like
'''
ner_list: 
len(ner_list):  221
[[1, 0, 'RT', 'R', 'O'],
 [1, 0, 'RT', 'T', 'O'],
 [1, 0, '@PeterRabbitt', '@', 'O'],
 [1, 0, '@PeterRabbitt', 'P', 'O'],
 [1, 0, '@PeterRabbitt', 'e', 'O'],
 [1, 0, '@PeterRabbitt', 't', 'O'],
 [1, 0, '@PeterRabbitt', 'e', 'O'],
'''

# this is what ner_word_list looks like
'''
ner_word_list: 
len(ner_word_list):  50
[[1, 1, 'RT', 'O'],
 [1, 2, '@PeterRabbitt', 'O'],
 [1, 3, ':', 'O'],
 [1, 4, 'HAPPY', 'O'],
 [1, 5, 'BIRTHDAY', 'O'],
 [1, 6, 'TO', 'O'],
 [1, 7, '@DaDaDaphne', 'O'],
 [1, 8, 'WISHIN', 'O'],
 [1, 9, 'YOU', 'O'],
 [1, 10, 'THE', 'O']]
'''


def add_class(datalist, tclass1_loc, logp):
    """
    add newly defined class.  Example:  mention, url
    tclass1_loc = token location in array of original class, depends on structure of list
    """
    newlist = []
    changect = 0
    # identify records with a change in class
    for item in datalist:
        change = 0
        token=item[2]
        # add class for twitter mention
        if token[0] == "@":
            tclass2 = "B-mention"
            changect += 1
            change = 1
        elif token.startswith("http"):
            # Add a class for url links
            tclass2 = "B-url"
            changect += 1
            change = 1
        else:
            tclass2 = item[tclass1_loc]
            change = 0

        # print any items where classes were changed, as a check
        if logp == 1:
            if change == 1:
                print "changed:   ", item

        item.append(tclass2)
        newlist.append(item)
        
    print "--------------------------------------"
    print "number of changes:  ", changect
    print "newlist (with updated classes) "
    pprint(newlist[0:10])
    print "--------------------------------------"      
    return newlist

def add_tag_emoji(datalist, tclass1_loc, logp):
    """
    add new class/tag for emoji
    tclass1_loc = token location in array of original class/tag, depends on structure of list
    """
    print "hello, I'm in the tag_emoji function!"
    newlist = []
    changect = 0
    emoji_list = [":)", ":D", ";)", "(:x", "XD", ":-(", ":-)", ":-", ":]", ";-)", ":-p", \
                  "=/", "=)", ":O", "!:", ":/", ":\\", ":P", ":(", "&lt;", "&gt;" ]
    print emoji_list

    for item in datalist:
        change = 0
        token = item[2]
        tag2 = item[5]
        if token in emoji_list:
            change = 1
            changect += 1
            item[5] = 'B-emoji'
            print item

    print "number of emoji's: ", changect
    if logp == 1:
        print "printing log"
    '''
    newlist = []
    changect = 0
    # identify records with a change in class
    for item in datalist:
        change = 0
        token=item[2]
        # add class for twitter mention
        if token[0] == "@":
            tclass2 = "B-mention"
            changect += 1
            change = 1
        elif token.startswith("http"):
            # Add a class for url links
            tclass2 = "B-url"
            changect += 1
            change = 1
        else:
            tclass2 = item[tclass1_loc]
            change = 0

        # print any items where classes were changed, as a check
        if logp == 1:
            if change == 1:
                print "changed:   ", item

        item.append(tclass2)
        newlist.append(item)
        
    print "--------------------------------------"
    print "number of changes:  ", changect
    print "newlist (with updated classes) "
    pprint(newlist[0:10])
    print "--------------------------------------"      
    return newlist
    '''
    return


def output_file(datalist, out_filename):
    """
    write out list to workable tsv file name so it can be tested
    """
    with open(out_filename, "w") as fh:
            for row in datalist:
                # add a blank line before each tweet
                if row[1]==1:
                    fh.write("\n" + row[2] + "\t" + row[4] + "\n")
                else:
                    fh.write(row[2] + "\t" + row[4] + "\n")
                    
def output_file2(datalist, out_filename, ngram):
    """
    write out list to workable tsv file name so it can be tested
    """
    current = 1
    with open(out_filename, "w") as fh:
            for row in datalist:
                if row[0] != current:
                    fh.write("\n")
                    current = row[0]
                if row[1] == ngram:
                        # add a blank line before each tweet
                        if row[0]==1:
                                fh.write("\n" + row[2] + "\t" + row[3] + "\n")
                        else:
                                fh.write(row[2] + "\t" + row[3] + "\n")



# Note:  in original data file, the first line is not blank, but the last line is.
# check that list length matches output file length

# check number of lines in file
# wc -l *.tsv

# check that blank space has been added between tweets
# head -20 run2_recode_class.tsv

# remove first line in file
# tail -n +2 run2_recode_class.tsv > run2_recode_class_clean.tsv 


def create_dict(datalist, whichclass, logp):
    """
    put list in dictionary format in order to create ngrams
    logp = log print = print data for trouble-shooting
    """    
    # initialize dictionary
    dicttweet = defaultdict(list)

    # Fill in the entries one by one
    for line in datalist:
        setkey = tuple((line[0], line[1]))
        token = line[3]
        
        #if logp == 1:
        #    print setkey, token_class

        dicttweet[str(line[0])].append(line[whichclass])

        #print setkey

        if logp == 1:
            #print line
            pprint(dicttweet)

    return dicttweet

#----------------------------------------------
#  print dictionary
#----------------------------------------------

def printDict(dictname):
    print"\n------------------------------"
    print "len(dictionary): ", len(dictname)
    for k, v in dictname.items():
        print k, v

#printDict(d_bychar_char)
#printDict(d_bychar_tclass1)
#printDict(d_bychar_tclass2)



#----------------------------------------------
#  create ngrams
#----------------------------------------------
def create_ngrams(dict1, dict2, logp):
    """
    tkey = tweet number 
    tvalue = each character of tweet
    ckey = tweet number
    cvalue = class
    logp = log print = print for troubleshooting
    """
    ngrams_list = []
    for (tkey, tvalue), (ckey, cvalue) in izip(dict1.iteritems(), \
                                               dict2.iteritems()):
        tweet_length = sum(1 for v in tvalue if v)
        for gram_length in range(2, tweet_length+1):
            gramitems = ngrams(tvalue, gram_length)

            for index, grams in enumerate(gramitems, start=0):
                #print "\ngrams: ", grams
                #print "\tclass: ", cvalue[index]
                gramsjoined = "".join(grams)
                item = [tkey, gram_length, gramsjoined, cvalue[index]]
                ngrams_list.append(item)
                #print "item: ", item
                #print "gram_length: ", gram_length
                #print "grams: ", gramsjoined
        if logp == 1:
            #print "\ntweet_length: ", tweet_length
            #print tkey
            #print tvalue
            #print ckey
            #print cvalue

            print "\nmaximum-length gram: ", tweet_length
            print gramsjoined
            print cvalue[index]
            #pprint(ngrams_list)

    return ngrams_list

# Note: I am including the class that corresponds to letter at start of ngram
#       This will be adjusted later
# this is what ngrams list looks like: tweet number, ngram length, ngram, class at start of ngram
'''
[['1', 2, 'RT', 'O'],
 ['1', 2, 'T@', 'O'],
 ['1', 2, '@P', 'B-mention'],
 ['1', 2, 'Pe', 'B-mention'],
 ['1', 2, 'et', 'B-mention'],
 ['1', 2, 'te', 'B-mention'],
 ['1', 2, 'er', 'B-mention'],
 ['1', 2, 'rR', 'B-mention'],
 ['1', 2, 'Ra', 'B-mention'],
 ['1', 2, 'ab', 'B-mention'],
 ['1', 2, 'bb', 'B-mention'],
 ['1', 2, 'bi', 'B-mention'],
 ['1', 2, 'it', 'B-mention'],
'''

if __name__ == '__main__':
    """
    function input:  train or dev datafiles
    function returns:  by char list, by word list
    train    : 36,695 lines
    test(dev): 12,170 lines
    """

    '''
    # Pablo's additions:  comment out for now while I work on emoji tag
    ner_list_train, ner_word_list = read_data("../../wnut_ner_evaluation/data/train", 0)
    ner_list_dev, ner_word_list = read_data("../../wnut_ner_evaluation/data/dev", 0)
    '''
    
    # use data (some small subsets to test code)
    #ner_list, ner_word_list = read_data("../data/lines25.iob", 1)
    #ner_list, ner_word_list = read_data("../data/lines50.iob", 1)
    #ner_list = read_data("../data/lines60.iob", 0)
    #ner_list = read_data("../data/line350.iob", 0)
    ner_list, ner_word_list = read_data("../data/all.iob", 1)

    ner_list_run2 = add_class(ner_list, 4, 0)
    ner_list_run3 = add_tag_emoji(ner_list_run2, 4, 0)
    #ner_list_for_output_file = add_class(ner_word_list, 3, 0)



    '''
    # Pablo's additions: comment out for now while I get emoji tag ready

    d_bychar_char_train = create_dict(ner_list_train, 3, 0)
    d_bychar_tclass1_train = create_dict(ner_list_train, 4, 0)

    d_bychar_char_dev = create_dict(ner_list_dev, 3, 0)
    d_bychar_tclass1_dev = create_dict(ner_list_dev, 4, 0)
    
    ngrams_list_class1_train = create_ngrams(d_bychar_char_train, d_bychar_tclass1_train, 0)
    ngrams_list_class1_dev = create_ngrams(d_bychar_char_dev, d_bychar_tclass1_dev, 0)

    output_file2(ngrams_list_class1_train, "../../wnut_ner_evaluation/data/train_4gram", 4)
    output_file2(ngrams_list_class1_dev, "../../wnut_ner_evaluation/data/dev_4gram", 4)
    '''
