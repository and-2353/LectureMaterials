# スーパーの在庫管理システムを作りたい
# 商品ごとに 商品名、価格、在庫数のデータを保存しておきたい

# listを使おう と思いつく
# 登録用のプログラムは省くが、こんなリストができそう
product_list = [['cake', 300, 20],
                ['computer', 50000, 3],
                ['coffee', 100, 100]]
                
"""
# これはあんまりスマートじゃない...
# (実際には表(pandasのdataframeなど)にして管理する方法が現実的ではある)
import pandas as pd
product_columns = ['name', 'price', 'stock']
product_df = pd.DataFrame(data=product_list, columns=product_columns)
print(product_df)
"""

# MyProduct クラスを定義する方法を取ってみる
class MyProduct:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

product1 = MyProduct('cake', 300, 20)
product2 = MyProduct('computer', 50000, 3)
product3 = MyProduct('coffee', 100, 100)

print('\n')
print(product1) # これだけ見ると分かりづらい気もする
print(type(product1))
print(product1.name, product1.price, product1.stock) # この書き方で値にアクセスできること、最高にスマートだと思います
