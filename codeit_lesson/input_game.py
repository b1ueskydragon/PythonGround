# 問題にはないけど、例外処理 + 独自定義 追加

from random import randint as rd

ans = rd(1, 20)
cnt = 4


class ZeroToTwenty(Exception):
    def message(self):
        print("Please re-enter your number between 1 to 20")

while cnt < 5:
    try:
        put_num = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % cnt))
        if not 20 >= put_num >= 1:
            raise ZeroToTwenty
        else:
            cnt -= 1

            if ans > put_num:
                print("UP")
            if ans < put_num:
                print("DOWN")
            if ans == put_num:
                print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (4 - cnt))
                break
            if cnt == 0 and cnt != ans:
                print("아쉽습니다. 정답은 %d였습니다." % ans)
                break

    except ValueError:
        print("Please input a number <class 'int'>.")
    except ZeroToTwenty as e:
        e.message()
