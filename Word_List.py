import random

Word_List= open('Word_List','r')
all_words= Word_List.readlines()
word_list= []
for i in all_words:
    word_list.append(i)

word_list = [x[:-1] for x in word_list]
#print(word_list)


