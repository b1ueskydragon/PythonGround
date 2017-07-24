# 参考 http://cortyuming.hateblo.jp/entry/20081208/p3
try:
    for c in range(5):
        print(c)
        assert c != 3
except:  # pythonのcatchみたいなやつ
    print("except: %d" % c)