from thinkgood import Thinkgood
from campusmon import Campusmon

if __name__ == '__main__':
    thinkgood = Thinkgood()

    print("===== thinkgood crawling =====")
    thinkgood.crawling()

    print("===== thinkgood list =====")
    thinkgood.check_result()
