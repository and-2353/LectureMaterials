import torch
import torch.nn as nn
import torch.optim as optim
from intro_2 import MLPNet

device = 'cuda' if torch.cuda.is_available() else 'cpu'
net = MLPNet().to(device)


criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

"""
損失関数, optimizer をきめる

損失関数
    今回は分類問題, 多クラスの分類で良いとされてるCrossEntropy誤差を使う
    魚本4.2.2 を参照
optimizer
    SGD(確率的勾配降下法)
    魚本6章 を参照
    ネットワークのパラメータと学習率を指定しないといけない
    モーメント, 重み減衰なども指定可能
"""

"""
ライブラリを使うときはGoogle検索するとライブラリのページが大体出てくる。

引数は絶対必要なものと, オプションのものがある
引数は取れる型が決まってるので何型を入れないといけないか分かってないとエラーになる。
指定しなかった場合の初期値なども公式のスクリプトに書いてあるので参照しながら使ってください

今回は torch.optim.SGD で検索すると 
https://pytorch.org/docs/stable/generated/torch.optim.SGD.html
がヒットしました。
"""