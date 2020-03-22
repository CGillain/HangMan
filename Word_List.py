import random

Word_List= open('Word_List','r')
all_words= Word_List.readlines()
word_list= []
for i in all_words:
    word_list.append(i)

word_list = [x[:-1] for x in word_list]

new_word_list= []
for j in word_list:
    new_word_list.append(j.lower())
#print(new_word_list)


