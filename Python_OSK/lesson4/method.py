# 引数を持たず、返り値を持たない関数 
def printError():
    print('エラーが発生しました')

# 引数を持ち、返り値を持たない関数
def printErrorpoint(a):
    print(f'{a}行目でエラーが発生しました')

# 引数を持ち、返り値を持つ関数
def multiplication(a:int, b:int):
    x = a * b
    return x

# 使い方
printError()
printErrorpoint(2)

# 返り値を持つ関数は代入形式で使われることが多い
y = multiplication(3, 4)
