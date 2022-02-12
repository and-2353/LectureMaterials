# ネットワーク定義

"""
・どんな層を作るか
    全結合層, 畳み込み層(お魚本7章), 活性化関数, など...
・どう並べるか
    行列積は連続で並べちゃいけなかったね
・何層作るか
    一般に深いほうが表現力が上がるけど、学習に時間がかかる
・隠れ層のサイズ
    行列積はサイズが違うと定義できないので, サイズを調整しないとエラーになる
    
    などを定義する

Pytorch では2つの書き方がある
1. nn.Seaquential
2. nn.Module

今回は 2. nn.Module で書く
"""

"""
MNISTは28*28のグレースケール画像, 取り込まれたときは(28*28)の2次元テンソル(行列)
それを(784)の1次元テンソルにして、ネットワークへの入力とする
そしたら画像の縦のつながりは消えてしまうので、分類の精度は期待できない(それでも75% とかは行く)
周辺情報が失われることは、畳み込み層(魚本7章)などで改善できる
実際、畳み込み層を使った方が精度が高くなる

ちなみに, グレースケール画像はチャンネル数が1だけど, RGB画像はチャンネル数が3
なので、画像をテンソル化したときのサイズが(28*28*3)とかになる。
"""

import torch
import torch.nn as nn
import torch.nn.functional as f

class MLPNet(nn.Module):
    def __init__(self):
        super(MLPNet, self).__init__()
        self.fc1 = nn.Linear(784, 600) # (784) * (784, 600) -> (600)
        self.fc2 = nn.Linear(600, 10) # (600) * (600, 10) -> (10)
        # 出力は(1, 10)の1次元ベクトルになる
        # 注：途中で活性化関数を通すが, 活性化関数を通してもテンソルの形状は変化しない
        
    def forward(self, x):
        x = self.fc1(x)
        x = torch.sigmoid(x)
        x = self.fc2(x)
        x = f.softmax(x, dim=1)
        return x

device = 'cuda' if torch.cuda.is_available() else 'cpu'
net = MLPNet().to(device)


