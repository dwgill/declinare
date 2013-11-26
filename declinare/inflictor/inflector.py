#!/usr/bin/env python
# vim: set fileencoding=UTF-8

from __future__ import unicode_literals
from collections import namedtuple
from collections import defaultdict

Case = namedtuple('Case', ['name','suffix','suffix_length'])

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

_case('first_nom_sg', 'a')
_case('first_gen_sg', 'ae')
_case('first_dat_sg', 'ae')
_case('first_acc_sg', 'am')
_case('first_abl_sg', 'a')
_case('first_nom_pl', 'ae')
_case('first_gen_pl', 'arum')
_case('first_dat_pl', 'is')
_case('first_acc_pl', 'as')
_case('first_abl_pl', 'is')
_case('second_nom_sg', 'us')
# Second delension words can sometimes have irregular nominative forms
_case('second_nom_sg', '')
_case('second_gen_sg', 'i')
_case('second_dat_sg', 'o')
_case('second_acc_sg', 'um')
_case('second_abl_sg', 'o')
_case('second_nom_pl', 'i')
_case('second_gen_pl', 'orum')
_case('second_dat_pl', 'is')
_case('second_acc_pl', 'os')
_case('second_abl_pl', 'is')
# Third declension nominative signulars are always irregular
_case('third_nom_sg', '')
_case('third_gen_sg', 'is')
_case('third_dat_sg', 'i')
_case('third_acc_sg', 'em')
_case('third_abl_sg', 'e')
_case('third_nom_pl', 'es')
_case('third_gen_pl', 'um')
_case('third_dat_pl', 'ibus')
_case('third_acc_pl', 'es')
_case('third_abl_pl', 'ibus')
_case('fourth_nom_sg', 'us')
_case('fourth_gen_sg', 'us')
_case('fourth_dat_sg', 'ui')
_case('fourth_acc_sg', 'um')
_case('fourth_abl_sg', 'u')
_case('fourth_nom_pl', 'us')
_case('fourth_gen_pl', 'uum')
_case('fourth_dat_pl', 'ibus')
_case('fourth_acc_pl', 'us')
_case('fourth_abl_pl', 'ibus')
_case('fifth_nom_sg', 'es')
_case('fifth_gen_sg', 'ei')
_case('fifth_dat_sg', 'ei')
_case('fifth_acc_sg', 'em')
_case('fifth_abl_sg', 'e')
_case('fifth_nom_pl', 'es')
_case('fifth_gen_pl', 'erum')
_case('fifth_dat_pl', 'ebus')
_case('fifth_acc_pl', 'es')
_case('fifth_abl_pl', 'ebus')
