class Hoge(object):
    a = "global var"

    def __init__(self):
        self.a = "local var"  # selfによりインスタンス変数になる(インスタンスにバウンドされる)
        a = "nothing"


print(Hoge.a)
hoge = Hoge()
print(type(hoge))
print(type(hoge.a))
print(type(Hoge.a))
print(hoge.a)

print(hoge.__dict__)
