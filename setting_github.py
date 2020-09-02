# -*- encoding: utf-8 -*-

import os
from github import Github
from pytz import timezone
from datetime import datetime

from utils import save, load


def get_github_repo(access_token, repository_name):
    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)
    return repo


def upload_github_issue(repo, open):
    already_opened = [elem.title for elem in repo.get_issues(state='open')]
    for key, val in open.items():
        if key not in already_opened:
            issue_title = key
            upload_contents = "* 기간: %s\n * 분류: %s\n * 주최자: %s\n * 사이트링크: %s" % (val[0], val[1], val[2], val[3])
            repo.create_issue(title=issue_title, body=upload_contents)


def close_github_issue(repo, close):
    open_issues = repo.get_issues(state='open')
    KST = str(datetime.now(timezone('Asia/Seoul')))[:10]
    need_to_close = list(close.keys())
    for issue in open_issues:
        if issue.title in need_to_close:
            issue.edit(state='closed')
        if issue.body[18:29] < KST:
            issue.edit(state='closed')



if __name__ == "__main__":
    """ init settings """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "Realtime-IT-Contest-notification"
    repo = get_github_repo(access_token, repository_name)

    """ load data """
    open = load(base_dir, "/open.json")
    close = load(base_dir, "/close.json")

    """ setting issues """
    close_github_issue(repo, close)
    upload_github_issue(repo, open)
