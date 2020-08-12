# -*- encoding: utf-8 -*-
from incruit import Incruit
from thinkgood import Thinkgood
from kmp import KMP

import os
import json


def save(base_dir, contests):
    with open(os.path.join(base_dir, 'contests.json'), 'w+', encoding='utf-8') as json_file:
        json.dump(contests, json_file, ensure_ascii=False, indent='\t')
    print("===== Finish saving data... =====")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # """ init setting """
    # incruit = Incruit()
    # thinkgood = Thinkgood()
    #
    # """ crawling  & save contests data"""
    # incruit.crawling(), incruit.save()
    # thinkgood.crawling(), thinkgood.save()

    """ using [KMP Algorithm]"""
    with open(base_dir + "/incruit.json", encoding='utf-8', errors='ignore') as json_data:
        contests_incruit = json.load(json_data, strict=False)
    with open(base_dir + "/thinkgood.json", encoding='utf-8', errors='ignore') as json_data:
        contests_thinkgood = json.load(json_data, strict=False)
    kmp = KMP(contests_incruit, contests_thinkgood)
    kmp.check()

    """ save contest lists & using [KMP Algorithm] """
    save(base_dir, kmp.contests)
