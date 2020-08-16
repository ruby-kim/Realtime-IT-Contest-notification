from incruit import Incruit
from thinkgood import Thinkgood


if __name__ == "__main__":
    """ init setting """
    incruit = Incruit()
    # thinkgood = Thinkgood()

    """ crawling list """
    incruit.crawling()
    # thinkgood.crawling()

    """ print result """
    incruit.check_result()
    # thinkgood.check_result()

    """ check dir name """
    incruit.check_dirname()
    # thinkgood.check_dirname()
