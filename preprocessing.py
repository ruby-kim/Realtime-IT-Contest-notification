# -*- encoding: utf-8 -*-

import os
import re
import math
from collections import Counter
from pytz import timezone
from datetime import datetime

from utils import save, load
from copy import deepcopy


def text2vec(text):
    Word = re.compile(r'\w+')
    words = Word.findall(text)
    return Counter(words)


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


if __name__ == "__main__":
    """ init settings """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    KST = str(datetime.now(timezone('Asia/Seoul')))[:10]

    """ load data """
    contests_incruit = load(base_dir, "/incruit.json")
    contests_thinkgood = load(base_dir, "/thinkgood.json")

    """ check duplicate titles """
    result = deepcopy(contests_thinkgood)
    for thinkgood_key, thinkgood_val in contests_thinkgood.items():
        vec1 = text2vec(thinkgood_key)
        flag = 0
        key, value = None, None
        for incruit_key, incruit_val in contests_incruit.items():
            vec2 = text2vec(incruit_key)
            cosine = get_cosine(vec1, vec2)
            if cosine >= 0.5:
                continue
            else:
                key = incruit_key
                value = incruit_val
                flag = 1
        if flag:
            result[key] = value

    """ separate data based on DATE """
    open = dict()
    close = dict()
    for key, val in result.items():
        if val[0][13:] < KST:
            close[key] = val
        else:
            open[key] = val

    """ save data """
    save(base_dir, open, 'open.json')
    save(base_dir, close, 'close.json')
