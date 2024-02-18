#1. Word Counter:
# Write a program that reads a sentence and counts the number of times
#each word appears.Use a dictionary to store the word counts.
def word_counter():
    sentence=input("enter any sentence:")
    dicta={}  #it will store our key-value pair
    #to count the number of times words are used
    for word in sentence.split():  #it will split each word and assign it to word
        count=1
        if word not in dicta: 
            count=1
            dicta[word]=count # add a new key value pair,will take word as key and
                            # its repetition as value
        else:
            count+=1
            dicta[word]=count
    print(dicta)
word_counter()