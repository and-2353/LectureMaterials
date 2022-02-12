# データについて

"""
ネットでデータセットをダウンロードするのが普通(?)
有名なデータセットはPytorchのライブラリtorchvisionで呼び出すことができる。
"""
import torch
from torchvision.datasets import MNIST
from torchvision import transforms

trainset = MNIST(root='./data', train=True, download=True, transform=transforms.ToTensor())
testset = MNIST(root='./data', train=False, download=True, transform=transforms.ToTensor())
print(type(trainset[0][0]))
"""
実行すると, data ディレクトリが作成され、そこにデータがダウンロードされる。

root= './data'
    データセットを保存するディレクトリ
    「.」は自分がいるところを意味。
train=True
    Trueの場合, トレーニングデータ
    Falseの場合, テストデータ
download=True
    Trueの場合, データをダウンロードする(そして指定したディレクトリに保存する。)
transform=transforms.toTensor()
    torch.Tensor型にtransformしてから読み込む

中身や形状, 型を見てみてください, 行列とラベルがあるのが確認できるはずです
"""

# データローダーの宣言
train_loader = torch.utils.data.DataLoader(dataset=trainset, batch_size=50, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=testset, batch_size=50, shuffle=False)

"""
ミニバッチ学習(魚本4.2.3 参照)をしたいので、ランダムでバッチサイズだけ
画像をサンプルしてくれるデータローダーを宣言しておく

これにより、50枚の画像をネットワークに通して、Lossの値の平均を取って
これをもとにパラメータを更新する

(画像1枚をもとに更新するよりミニバッチをもとに更新したほうが、
変な方向に間違って更新することが減って学習がスムーズそう)
"""