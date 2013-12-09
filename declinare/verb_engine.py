#!/usr/bin/env python
# vim: set fileencoding=UTF-8

from __future__ import unicode_literals
from collections import namedtuple
from collections import defaultdict

Decl = namedtuple('Decl', ['name','suffix','suffix_length'])

_verb_decls = {}
_max_suffix_length = 5 #erunt is longest?

def _decl(name, suffix):
    decl = decl(name,suffix, len(suffix))
    _verb_decls.setdefault(suffix,[]).append(decl)

def get_decl(word):
    def get(it): return _verb_decls.get(it,[])

    for decl in get(''):
        yield decl
    for length in range(1, min(_max_suffix_length + 1, len(word))):
        for decl in get(word[-length:]):
            yield decl

#first
#indicative
#active
#based of infinitive
_decl('first_indi_act_present_1s','o')
_decl('first_indi_present_2s','s')
_decl('first_indi_act_present_3s','t')
_decl('first_indi_act_present_1p','mus')
_decl('first_indi_act_present_2p','tis')
_decl('first_indi_act_present_3p','nt')
_decl('first_indi_act_imperfect_1s','bam')
_decl('first_indi_act_imperfect_2s','bas')
_decl('first_indi_act_imperfect_3s','bat')
_decl('first_indi_act_imperfect_1p','bamus')
_decl('first_indi_act_imperfect_2p','batis')
_decl('first_indi_act_imperfect_3p','bant')
_decl('first_indi_act_future_1s','bo')
_decl('first_indi_act_future_2s','bis')
_decl('first_indi_act_future_3s','bit')
_decl('first_indi_act_future_1p','bimus')
_decl('first_indi_act_future_2p','bistis')
_decl('first_indi_act_future_3p','bint')
#based off 3rd principle part
_decl('first_indi_act_perfect_1s','i')
_decl('first_indi_act_perfect_2s','isti')
_decl('first_indi_act_perfect_3s','it')
_decl('first_indi_act_perfect_1p','imus')
_decl('first_indi_act_perfect_2p','istis')
_decl('first_indi_act_perfect_3p','erunt')
_decl('first_indi_act_pluperfect_1s','eram')
_decl('first_indi_act_pluperfect_2s','eras')
_decl('first_indi_act_pluperfect_3s','erat')
_decl('first_indi_act_pluperfect_1p','eramus')
_decl('first_indi_act_pluperfect_2p','eratis')
_decl('first_indi_act_pluperfect_3p','erant')
_decl('first_indi_act_futureperfect_1s','ero')
_decl('first_indi_act_futureperfect_2s','eris')
_decl('first_indi_act_futureperfect_3s','erit')
_decl('first_indi_act_futureperfect_1p','erimus')
_decl('first_indi_act_futureperfect_2p','eritis')
_decl('first_indi_act_futureperfect_3p','erunt')
#passive
_decl('first_indi_pas_present_1s','or')
_decl('first_indi_pas_present_2s','ris')
_decl('first_indi_pas_present_3s','tur')
_decl('first_indi_pas_present_1p','mur')
_decl('first_indi_pas_present_2p','mini')
_decl('first_indi_pas_present_3p','ntur')
_decl('first_indi_pas_imperfect_1s','bar')
_decl('first_indi_pas_imperfect_2s','baris')
_decl('first_indi_pas_imperfect_3s','batur')
_decl('first_indi_pas_imperfect_1p','bamur')
_decl('first_indi_pas_imperfect_2p','bamini')
_decl('first_indi_pas_imperfect_3p','bantur')
_decl('first_indi_pas_future_1s','bor')
_decl('first_indi_pas_future_2s','beris')
_decl('first_indi_pas_future_3s','bitur')
_decl('first_indi_pas_future_1p','bimur')
_decl('first_indi_pas_future_2p','bimini')
_decl('first_indi_pas_future_3p','buntur')
#perfect
_decl('first_indi_pas_perfect_1s','parts sum')
_decl('first_indi_pas_perfect_2s','parts es')
_decl('first_indi_pas_perfect_3s','parts est')
_decl('first_indi_pas_perfect_1p','partp sumus')
_decl('first_indi_pas_perfect_2p','partp estis')
_decl('first_indi_pas_perfect_3p','partp sunt')
_decl('first_indi_pas_pluperfect_1s','parts eram')
_decl('first_indi_pas_pluperfect_2s','parts eras')
_decl('first_indi_pas_pluperfect_3s','parts erant')
_decl('first_indi_pas_pluperfect_1p','partp eramus')
_decl('first_indi_pas_pluperfect_2p','partp eratis')
_decl('first_indi_pas_pluperfect_3p','partp erant')
_decl('first_indi_pas_futureperfect_1s','parts ero')
_decl('first_indi_pas_futureperfect_2s','parts eris')
_decl('first_indi_pas_futureperfect_3s','parts erit')
_decl('first_indi_pas_futureperfect_1p','partp erimus')
_decl('first_indi_pas_futureperfect_2p','partp eritis')
_decl('first_indi_pas_futureperfect_3p','partp erunt')
#subjunctive
#active
_decl('first_subj_act_present_1s','*m') #for present 1->e 2->ea 3->a 4->ia
_decl('first_subj_present_2s','*s')
_decl('first_subj_act_present_3s','*t')
_decl('first_subj_act_present_1p','*mus')
_decl('first_subj_act_present_2p','*tis')
_decl('first_subj_act_present_3p','*nt')
_decl('first_subj_act_imperfect_1s','rem')
_decl('first_subj_act_imperfect_2s','res')
_decl('first_subj_act_imperfect_3s','ret')
_decl('first_subj_act_imperfect_1p','remus')
_decl('first_subj_act_imperfect_2p','retis')
_decl('first_subj_act_imperfect_3p','rent')
# 3rd principle part
_decl('first_subj_act_perfect_1s','erim') #no future subjunctive
_decl('first_subj_act_perfect_2s','eris')
_decl('first_subj_act_perfect_3s','erit')
_decl('first_subj_act_perfect_1p','erimus')
_decl('first_subj_act_perfect_2p','eritis')
_decl('first_subj_act_perfect_3p','erint')
_decl('first_subj_act_pluperfect_1s','issem')
_decl('first_subj_act_pluperfect_2s','isses')
_decl('first_subj_act_pluperfect_3s','isset')
_decl('first_subj_act_pluperfect_1p','issemus')
_decl('first_subj_act_pluperfect_2p','issetis')
_decl('first_subj_act_pluperfect_3p','issent')
#passive
_decl('first_subj_pas_present_1s','*r') #for present 1->e 2->ea 3->a 4->ia
_decl('first_subj_pas_present_2s','*ris')
_decl('first_subj_pas_present_3s','*tur')
_decl('first_subj_pas_present_1p','*mur')
_decl('first_subj_pas_present_2p','*mini')
_decl('first_subj_pas_present_3p','*ntur')
_decl('first_subj_pas_imperfect_1s','rer')
_decl('first_subj_pas_imperfect_2s','reris')
_decl('first_subj_pas_imperfect_3s','retur')
_decl('first_subj_pas_imperfect_1p','remur')
_decl('first_subj_pas_imperfect_2p','remini')
_decl('first_subj_pas_imperfect_3p','rentur')
_decl('first_subj_pas_perfect_1s','parts sim')
_decl('first_subj_pas_perfect_2s','parts sis')
_decl('first_subj_pas_perfect_3s','parts sit')
_decl('first_subj_pas_perfect_1p','partp simus')
_decl('first_subj_pas_perfect_2p','partp sitis')
_decl('first_subj_pas_perfect_3p','partp sint')
_decl('first_subj_pas_pluperfect_1s','parts essem')
_decl('first_subj_pas_pluperfect_2s','parts esses')
_decl('first_subj_pas_pluperfect_3s','parts esset')
_decl('first_subj_pas_pluperfect_1p','partp essemus')
_decl('first_subj_pas_pluperfect_2p','partp essetis')
_decl('first_subj_pas_pluperfect_3p','partp essent')
#imperative
#active
_decl('first_imperative_act_pres_s','*') *=stem
_decl('first_imperative_act_pres_p','*te')
_decl('first_imperative_act_fut_2s','*to')
_decl('first_imperative_act_fut_2p','*tote')
_decl('first_imperative_act_fut_3s','*to')
_decl('first_imperative_act_fut_3p','*nto')
#passive
_decl('first_imperative_pas_pres_s','*re')
_decl('first_imperative_pas_pres_p','*mini')
_decl('first_imperative_pas_fut_2s','*tor')
_decl('first_imperative_pas_fut_3s','*tor')
_decl('first_imperative_pas_fut_3p','*ntor')
