from thinkgood import Thinkgood
from campusmon import Campusmon
import pandas as pd

if __name__ == '__main__':
    thinkgood = Thinkgood()

    print("===== thinkgood crawling =====")
    thinkgood.crawling()

    print("===== thinkgood list =====")
    # thinkgood.check_result()

    df = pd.DataFrame(thinkgood.infos).T
    df.rename(columns={0 :'기간', 1 : '분야', 2 : '주최', 3 : '링크'}, inplace=True)

    print(df)

