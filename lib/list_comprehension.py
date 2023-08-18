#!/usr/bin/env python3

def return_evens(num_list):

   even_num=num_list
   even_nos = [num for num in even_num if num % 2 == 0]
   return even_nos

return_evens([0,1, 3, 5, 7, 8, 9])



def make_exclamation(sentence_list):

   sentence_plus_exclamation=sentence_list
   new_list = [sentence+'!' for sentence in sentence_plus_exclamation]
   return new_list

make_exclamation(["Hello", "I'm doing great", "Python is fun"])