#!/usr/bin/env python
# vim: set fileencoding=UTF-8

from __future__ import unicode_literals
from collections import namedtuple
from collections import defaultdict

# Define a subclass of tuple that allows access to its elements like 
# they're instance variables. my_inflection.stem, my_inflection.suffix, etc.
Inflection = namedtuple('Inflection', ['stem', 'grammar_group', 'suffix'])

class Inflector(object):
    """
    A class that lists the possible inflections of a word within the given
    categories.
    """

    def __init__(self, inflections):
        # A dict of suffixes to lists of grammar_group's
        self.grammar_groups = {}

        # The longest length of a suffix we have found.

        self.max_length = 0
        for grammar_group, suffix in inflections:
            # Try to get a value for the key suffix. If the key is not
            # found, then put it in the dict as being associated with an
            # empty list. Then return the value associated with that key.
            grammar_groups = self.grammar_groups.setdefault(suffix, [])
            # Add a new grammar_group, suffix pair to the list of
            # grammar_groups associated with suffix.
            grammar_groups.append(grammar_group)
            # Update local max.
            self.max_length = max(self.max_length, len(suffix))

    def inflect(self, word):
        """
        Return all the possible inflections for word per the
        schema provided to this inflector.
        """
        word = word.lower()
        inflections = []

        for length in range(1,min(self.max_length + 1, len(word))):
            stem, suffix = word[:-length], word[-length:]
            gg_for_suffix = self.grammar_groups.get(suffix,[])
            inflections.extend(Inflection(stem, gg, suffix)
                    for gg in gg_for_suffix)

        return inflections
