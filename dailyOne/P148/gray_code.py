def gray_code(bit: int, codes=[]) -> list:
    # 後に隣接する符号間のハミング距離が必ず1になるような順番
    # XOR した結果が前後とも 01 or 10 (2bit の場合)
    # n bit, 2^0 ~ 2^(n-1) 取り得るハミング距離

    return codes


print(gray_code(bit=2))

print(0 ^ 1)  # 01
print(1 ^ 3)  # 10
print(3 ^ 2)  # 01