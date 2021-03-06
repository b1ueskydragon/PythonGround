#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

CK = 'XXXXXXXXXXXXXXXXXXXXXX'                             # Consumer Key
CS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'         # Consumer Secret
AT = 'XXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' # Access Token
AS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'         # Accesss Token Secert

# タイムライン取得用のURL
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# とくにパラメータは無い
params = {}

# OAuth で GET
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.get(url, params = params)

if req.status_code == 200:
    # レスポンスはJSON形式なので parse する
    timeline = json.loads(req.text)
    # 各ツイートの本文を表示
    for tweet in timeline:
        print(tweet["text"])

else:
    # エラーの場合
    print ("Error: %d" % req.status_code)