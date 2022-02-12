# リストライクなオブジェクト

"""
Python 標準のリスト
"""
list_1 = [1, 2, 3, 4, 5]

print('-------------')
print('list_1: ', list_1)
print('list_1_type: ', type(list_1))
print('-------------')


"""
numpy のndarray
"""
import numpy as np
list_2 = np.array([1, 2, 3, 4, 5])
list_3 = np.zeros(5)
print('list_2: ', list_2)
print('list_2_type: ', type(list_2))
print('-------------')
print('list_3: ', list_3)
print('list_3_type: ', type(list_3))
print('-------------')


"""
Pytorch のtorch.Tensor
"""
import torch
list_4 = torch.tensor([1, 2, 3, 4, 5])
list_5 = torch.zeros([5])
print('list_4: ', list_4)
print('list_4_type: ', type(list_4))
print('-------------')
print('list_5: ', list_5)
print('list_5_type: ', type(list_5))
print('-------------')

"""
性質 にてる
Pytorchのメソッド使うときは torch.Tensor を加工していく
データセットや画像を torch.Tensor として取り込む
(Python標準のリストを引数とするとエラーになったりする)
性質が似てるので、メソッドに使うために形式を変換することもよく行われる
"""
