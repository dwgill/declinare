#!/usr/bin/env python 
# vim: set fileencoding=UTF-8
from __future__ import unicode_literals
from inflector import Inflector
from noun_data import noun_data
from verb_data import verb_suffixes as verb_data
import re
import sys
import sqlite3
import os

noun_cases = Inflector(noun_data)
verb_forms = Inflector(verb_data)

def main():
    len_args = len(sys.argv[1:])
    if len_args == 0:
        print("No valid input.")
    elif len_args == 1:
        string = sys.argv[0]
        # words = string.decode('utf-8').split()
    else:
        pass
        # words = [word.decode('utf-8') for word in sys.argv[1:]]

    cursor = create_db()
    # proc_words(words)

def proc_words(words):
    print('~nouns~')
    for word in words:
      handle_noun(word)
#      handle_verb(word)
    cases_conj #(all the forms the word might be)



def handle_noun(word):
   string = "{word}: ".format(word=word)
   for case in noun_cases.inflect(word):
      string = string + '\n\t{case_name}: {word}-{suffix}'.format(word=word[:-case.suffix_length], case_name=case.name, suffix=case.suffix)
      print(word[:case.suffix_length]) # gets stem, put in database
   return string

#def handle_verb(word):
#   string = "{word}: ".format(word=word)
#   for form in verb_forms.inflect(word):
#      string = string + '\n\t{form_name}: {word}-{suffix}'.format(word=word[:-form.suffix_length], form_name=form.name, suffix=form.suffix)
#   return string

def create_db():
   db = sqlite3.connect('stems.db')
   c = db.cursor() #creates something to enter SQL commands
   # Create a table 'Stems' with 10 columns 
   # c.execute('''CREATE TABLE Stems (_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, Stem text, D1 long, D2 long, D3 long, D4 long, D5 long, VERB long)''')
   # return cursor to work with
   return c

def tally_db(stem, cases_conjs, cursor):
   cursor.execute("SELECT _id FROM Stems WHERE Stem = ?",[stem])
   if cursor.rowcount <= 0: # stem is not in database
      c.execute("INSERT INTO Stems (Stem, D1, D2, D3, D4, D5, VERB) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(stem, 0, 0, 0, 0, 0, 0)) # the last 9 ?s are unnecessary
   for case_conj in cases_conjs:
      # TODO loop through every case and conj and tally it for that stem in the database      
      pass

if __name__ == "__main__":
    main()
