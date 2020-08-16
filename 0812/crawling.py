# -*- encoding: utf-8 -*-

from incruit import Incruit
from thinkgood import Thinkgood


if __name__ == "__main__":
    """ init setting """
    incruit = Incruit()
    thinkgood = Thinkgood()

    """ crawling  & save contests data"""
    incruit.crawling(), incruit.save_result()
    thinkgood.crawling(), thinkgood.save_result()
