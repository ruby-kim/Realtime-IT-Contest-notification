from detizen import Detizen
from jungle import Jungle


if __name__ == "__main__":
    """ init setting """
    detizen = Detizen()
    jungle = Jungle()

    """ crawling list """
    detizen.crawling()
    jungle.crawling()

    """ print result """
    # detizen.check_result()
    jungle.check_result()
