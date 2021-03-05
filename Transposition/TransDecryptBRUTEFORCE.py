#Python program to brute force decrypt a transposition cipher
#Dominic WOejwodka 
#March 2021

#Uses a file, englishWords.txt which contains 470k+ english words used for english recognition
#Credit for this dictionary: https://github.com/dwyl/english-words/blob/master/words.txt 

#dictionary
#file which opens the dictionary and stores the contents in an array
def dictionary():
    dictionaryFile = open("../englishWords.txt")
    dictionaryFile = dictionaryFile.read().splitlines()
    
    words = []
    for i in dictionaryFile:
        words.append(i)
    return words

#isEnglish
#this function will take a string and determine if it is english
#a standard ratio is passed as a parameter for the percentage of english that are required to be marked as english
def isEnglish(text,dictionary,ratio):
    #first convert the string into an array
    text = text.split(" ")
    length = len(text)
    count = 0
    #checks the words against the dictionary, counting the number of english words
    for i in text:
        if i in dictionary:
            count += 1
    #ratio of english to non english words
    PERCENT_ENGLISH = count/length
    print("Percent English: ", PERCENT_ENGLISH)
    if (PERCENT_ENGLISH >= ratio):
        return True
    else:
        return False
    
        

###
#main
words = dictionary()
print(isEnglish("The Quick Brown Fox Jumped Over The Lazy Dog",words,0.80))
