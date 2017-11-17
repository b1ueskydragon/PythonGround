#!/usr/bin/env pytnon3
# -*- coding: utf-8 -*-

from random import randint


# このゲームを1回実行する
# change_door True ならドアを変更、False なら変更しない
def game(change_door=False):
    prize = randint(0, 2)  # 正解のドア
    choice = randint(0, 2)  # 最初に選択するドア

    # 未選択、かつ、政界ではないドアの1つをランダムに選択
    while True:  # モンティが開くドアの決定
        open_door = randint(0, 2)
        if open_door != choice and open_door != prize:
            break

    if change_door:  # 選択を変更する場合
        for new_choice in range(3):  # 未洗濯でまだあいていないドアを選ぶ
            if new_choice != choice and new_choice != open_door:
                break
        choice = new_choice

    if choice == prize:  # 正解なら1点追加
        return 1
    else:
        return 0


def play(num, change_door):
    point = 0.0
    for _ in range(num):
        point += game(change_door)
    return point


num = 10_000  # ゲームの実行回数

score = play(num, False)
print(u'変更しない場合の勝率\t', score / num)

score = play(num, True)
print(u'変更した場合の勝率\t', score / num)
