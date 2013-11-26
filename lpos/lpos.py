#!/usr/bin/env python 
# vim: set fileencoding=UTF-8
from __future__ import unicode_literals
from noun_engine import get_cases
import re
import sys

def main():
    len_args = len(sys.argv)
    if len_args == 0:
        print("-- NO VALID INPUT --")
    elif len_args == 1:
        string = sys.argv[1]
        words = string.decode('utf-8').split()
    else:
        words = [word.decode('utf-8') for word in sys.argv[1:]]

    proc_words(words)

def proc_words(words):
    print('~nouns~')
    for word in words:
        print(handle_noun(word))

def handle_noun(word):
    string = "{word}: ".format(word=word)
    for case in get_cases(word):
        string = string + '\n\t{case_name}: ({suffix})'.format(case_name=case.name, suffix=case.suffix)
    return string



if __name__ == "__main__": main()
