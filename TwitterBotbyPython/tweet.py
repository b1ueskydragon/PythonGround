from requests_oauthlib import OAuth1Session  # Requests-OAuthlib ライブラリ
from TwitterBotbyPython.Keys.Keys import Keys

CK = Keys().CONSUMERKEY
CS = Keys().CONSUMERSECRET
AT = Keys().ACCESSTOKEN
AS = Keys().ACCESSTOKENSECRET

FROMBOT = " -- ちゃんbotより"

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
params = {"status": "勝手につぶやいちゃう" + FROMBOT}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
