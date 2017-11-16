# http://challenge-your-limits8.herokuapp.com/

# 秘密キー
# gon.d=" 37903";gon.n=" 89039";
d = 37903
n = 89039

# 暗号文
# gon.phrase=" [7655, 37396, 85672, 12881, 88682, 10155]";
phrase = [7655, 37396, 85672, 12881, 88682, 10155]

# RSA暗号の秘密鍵で暗号文->平文
# i** d % n でもとまる ascii を char に変換
access_code_is = ''.join(list(map(lambda i: chr(i ** d % n), phrase)))

print(access_code_is)
