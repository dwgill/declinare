#!/usr/bin/env python
from inflector import Inflector
from inflector import Inflection
from noun_data import noun_data
from verb_data import verb_suffixes as verb_data
import re
import sys
import sqlite3
import os
from irregwords import irregulars

noun_cases = Inflector(noun_data)
verb_forms = Inflector(verb_data)

def main():
    if len(sys.argv) < 1:
        print "I need a path."
        return
    path_to_training = sys.argv[1]
    db, c = create_db()
    words = list(process_dir(path_to_training))
    for index, inflection in enumerate(proc_words(words)):
        tally_db(inflection.stem, inflection.grammar_group, c, db)
        if index % 10000 == 0:
            db.commit()

def proc_words(words):
    global db
    count = 0
    total = 4097405.0
    for word in words:
        count += 1
        if count % 100 == 0:
            #print("=> " + word)
            print("=> " + str(count)+'('+str((count/total)*100) + "%)")

        if word in irregulars:
            yield Inflection(word, 'IRREGULAR', '')
        for inflection in handle_noun(word):
            yield inflection
        for inflection in handle_verb(word):
            yield inflection

def process_file(file_path):
    print("=> " + file_path)
    with open(name=file_path, mode='r') as open_file:
        for line in open_file:
            for word in tokenize(line):
                yield word

def tokenize(line):
    token_re = r"\w+"
    for match in re.findall(token_re, line):
        if len(match) > 1:
            yield match.lower()


def process_dir(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            for word in process_file(os.path.join(root, filename)):
                yield word

def handle_noun(word):
    return noun_cases.inflect(word)

def handle_verb(word):
    return verb_forms.inflect(word)

def create_db():
    db = sqlite3.connect('stems.db')
    c = db.cursor() #creates something to enter SQL commands
    # Create a table 'Stems' with 10 columns 
    c.execute('''CREATE TABLE IF NOT EXISTS Stems
            (_id INTEGER PRIMARY KEY AUTOINCREMENT
            NOT NULL UNIQUE, Stem text, NOUN long,
            VERB long, IRREGULAR long)''')
    # return cursor to work with
    return db, c

def tally_db(stem, gg, cursor, db):
    cursor.execute("SELECT _id FROM Stems WHERE Stem = ?",(stem,))
    indb = cursor.fetchone()
    if indb == None: #stem is not in database
        cursor.execute("INSERT INTO Stems (Stem, NOUN, VERB, IRREGULAR) VALUES ( ?, ?, ?, ?)",
                (stem, 0, 0, 0)) # the last 9 ?s are unnecessary
    cursor.execute("SELECT "+gg+" FROM Stems WHERE Stem = ?", (stem,))
    data = cursor.fetchone()
    count = int(data[0])
    count += 1
    cursor.execute("UPDATE Stems SET "+gg+"=? WHERE Stem = ?",
            (count, stem))



if __name__ == "__main__":
    main()
