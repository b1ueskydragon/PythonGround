# リスト内包表記
r=''.join(['パトカー'[i]+'タクシー'[i] for i in range(4)])  # リストの中でロジックを生成、2文字が1要素
print(r)


msg="パトカー"
msg_="タクシー"

result=''
# index, value
for i, v in enumerate(msg, 0):  # enumerate 関数 : 要素のインデックスと要素の両方を同時に取得
                          # 0 番 index からスタート
  result += msg[i]+msg_[i]
print(result)


msg1="パトカー"
msg2="タクシー"

result=''
for i,j in enumerate(msg1,0):
  result+=msg1[i]+msg2[i]
print(result)

stra = "パトカー"
strb = "タクシー"
strc = ""
lenstra = len(stra)
lenstrb = len(strb)
maxlen =  lenstra if lenstra > lenstrb else lenstrb

for i in range(maxlen):
    strc += stra[i] if lenstra > i else ""
    strc += strb[i] if lenstrb > i else ""

print(strc)
