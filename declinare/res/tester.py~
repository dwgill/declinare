#!/usr/bin/env python
import sys
import sqlite3

def run():
    if len(sys.argv) < 2:
        print "Please enter a word stem."
        return
    cursor = connect_to_db()
    stem = sys.argv[1]
    cursor.execute("SELECT * FROM Stems WHERE Stem = ?",(stem,))
    data = cursor.fetchone()
    print("( _id , Stem  ,  N,  V, IRR)")
    print data
    noun = int(data[2])
    verb = int(data[3])
    ireg = int(data[4])
    total = 0.0 + verb + noun + ireg
    print("Noun %: ") + str(noun*100 / total)
    print("Verb %: ") + str(verb*100 / total)
    print("Ireg %: ") + str(ireg*100 / total)
    
def connect_to_db():
    db = sqlite3.connect('stems.db')
    c = db.cursor() #creates something to enter SQL commands
    # return cursor to work with
    return c

if __name__ == '__main__':
    run()
