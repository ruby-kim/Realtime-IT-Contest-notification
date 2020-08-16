# Realtime-IT-Contest-notification
IT 공모전 실시간 알림 repository.<br>
3일에 한 번, KST 06:00 에 공모전 리스트를 업데이트 합니다.

### File Structure
```bash
.
|-- .github
|   └-- workflows
|       └-- setting.yml
|-- .gitignore
|-- 0729
|   |-- detizen.py
|   |-- jungle.py
|   └-- main.py
|-- 0731
|   |-- incruit.py
|   |-- main.py
|   |-- thinkgood.py
|   └-- wevity.py
|-- 0805
|   |-- incruit.py
|   |-- main.py
|   └-- thinkgood.py
|-- 0809
|   |-- github_utils.py
|   |-- incruit.json
|   |-- incruit.py
|   |-- kmp.py
|   |-- main.py
|   |-- thinkgood.json
|   └-- thinkgood.py
|-- 0812
|   |-- close.json
|   |-- crawling.py
|   |-- incruit.json
|   |-- incruit.py
|   |-- open.json
|   |-- preprocessing.py
|   |-- setting_github.py
|   |-- thinkgood.json
|   |-- thinkgood.py
|   └-- utils.py
|-- README.md
└-- requirements.txt
```

### Dev Environment
* python 3.6이상
* 필요 패키지 설치: ```pip install -r requirements.txt```

### Contest Site
* 씽굿: https://www.thinkcontest.com/
* 인크루트 공모전: http://gongmo.incruit.com/
