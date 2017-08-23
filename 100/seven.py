'''
テンプレートによる性成分

引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
'''


def template(x, y, z):
    x = str(x)
    y = str(y)
    z = str(z)
    return x + "時の" + y + "は" + z

print(template(12, "気温", 22.4))
