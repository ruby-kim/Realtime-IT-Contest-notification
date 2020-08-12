# -*- encoding: utf-8 -*-
from incruit import Incruit
from thinkgood import Thinkgood
from kmp import KMP

from github_utils import get_github_repo, upload_github_issue

import os
import json
# from datetime import datetime
# from pytz import timezone

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

    """ upload info to Issue """
    access_token = '76761b67fdbc31328943418649af46ada44c8e32'
    repository_name = "test"

    # seoul_timezone = timezone('Asia/Seoul')
    # today = datetime.now(seoul_timezone)
    # today_data = 'sssss'

    issue_title = f"test입니다" # f"test입니다({today_data})"
    upload_contents = 'testtt'
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("업로드 완료!")
