# 先程は在庫数を表すstockをインスタンス生成時に変数として渡していました。
# クラスインスタンス全てに持たせたい変数を固定で指定することもできます。

class MyProduct:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.sales = 0

myproduct1 = MyProduct('coffee', 100, 100)
print(myproduct1.stock)

# 初期化の関数がイニシャライザです。
# Pythonのイニシャライザは __init__ という名前で定義し、第一引数を selfにするという慣例があります。
# selfとはインスタンス本体のことで、selfを使用することでインスタンスが持つ他のメンバ変数を取得したり、
# メソッドを呼び出すことができます。
# 8 行目と12 行目の記述は似ていますよね。イニシャライザでメンバに変数を格納しているので、このように呼び出せるのです。

    