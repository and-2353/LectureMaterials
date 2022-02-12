class MyProduct:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.sales = 0

    def get_name(self): # 商品名メソッド
        return self.name
        
    def buy_up(self, n): # 仕入れメソッド
        self.stock += n

    def sell(self, n): # 販売メソッド
        self.stock -= n
        self.sales += n * self.price

    def summary(self): # 概要メソッド
        message = "called summary()." + \
        "\n name: " + self.get_name() + \
        "\n price: " + str(self.price) + \
        "\n stock: " + str(self.stock) + \
        "\n sales: " + str(self.sales)
        print(message)

myproduct1 = MyProduct('coffee', 100, 100)
myproduct1.summary()
myproduct1.sell(5)
myproduct1.summary()

# sell はMyProductクラスのインスタンスに対して、メンバを操作するメソッドです。
# summary は MyProductクラスのインスタンスに対して、メンバをprintするメソッドです。

# Python では def を使って関数を定義することができました。
# 引数を取る関数を定義する場合、作者は引数として入ってくるデータの型を想定しているはずです。
# それを示す方法もありました(型アノテーション)。
# でも、「このオブジェクトにしか使わない」という関数なら、バラバラに定義しておくよりも
# クラスメソッドとしてクラスの中に書いたほうが、第三者から見てわかりやすいと思います。
# 関数は独立して書かれるものなので、多くなるとわけわからなくなる。
# クラスメソッドとして表記することによって関数(メソッド)をグループ化できるわけです。