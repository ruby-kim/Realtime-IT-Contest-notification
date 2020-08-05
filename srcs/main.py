from thinkgood import Thinkgood
from campusmon import Campusmon

if __name__ == '__main__':
    campusmon = Campusmon()
    thinkgood = Thinkgood()

    print("===== campusmon crawling =====")
    campusmon.crawling()
    print("===== thinkgood crawling =====")
    thinkgood.crawling()

    print("===== campusmon list =====")
    campusmon.check_result()
    print("===== thinkgood list =====")
    thinkgood.check_result()
