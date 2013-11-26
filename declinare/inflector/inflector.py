#!/usr/bin/env python
# vim: set fileencoding=UTF-8

from __future__ import unicode_literals
from collections import namedtuple
from collections import defaultdict

Inflection = namedtuple('Inflection', ['name','suffix','suffix_length'])

_noun_cases = {}
_max_suffix_length = 4

def _case(name, suffix):
    case = Case(name,suffix, len(suffix))
    _noun_cases.setdefault(suffix,[]).append(case)

def get_cases(word):
    def get(it): return _noun_cases.get(it,[])

    for case in get(''):
        yield case
    for length in range(1, min(_max_suffix_length + 1, len(word))):
        for case in get(word[-length:]):
            yield case

class Inflector(object):
    def __init__(self, inflections, max_length):
        self.inflections = {}
        self.max_length = max_length
        def make_inflection(name, suffix):
            inflection = Inflection(name, suffix, len(suffix))
            self.inflections.setdefault(suffix, []).append(inflection)

    def inflect(self, word):
        inflections = []
        get = lambda suffix: self.inflections.get(suffix,[])

        inflections.extend(get(''))
        for length in range(1,min(self.max_length + 1, len(word))):
            inflections.extend(get(word[-length:]))

        return inflections
