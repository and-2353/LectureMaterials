import torch
import torch.nn as nn
import torch.optim as optim
from intro_2 import MLPNet
from torchvision.datasets import MNIST
from torchvision import transforms
import matplotlib.pyplot as plt

# デバイスの設定/ネットワークをインスタンス化
device = 'cuda' if torch.cuda.is_available() else 'cpu'
net = MLPNet().to(device)

# 損失関数と optimizer の決定
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# データローダーの設定
trainset = MNIST(root='./data', train=True, download=True, transform=transforms.ToTensor())
testset = MNIST(root='./data', train=False, download=True, transform=transforms.ToTensor())
train_loader = torch.utils.data.DataLoader(dataset=trainset, batch_size=50, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=testset, batch_size=50, shuffle=False)

# エポック数
num_epochs = 40

# matplotlib(画像プロット用ライブラリ)で使う為にリストを定義しておく
# 損失や正確率を適宜保存しておいて、あとでその変化を折れ線グラフにする
train_loss_list = []
train_acc_list = []
val_loss_list = []
val_acc_list = []


for epoch in range(num_epochs):
    train_loss = 0
    train_acc = 0
    val_loss = 0
    val_acc = 0

    net.train()
    for i, (images, labels) in enumerate(train_loader):
        # 画像を1次元にする
        images = images.view(-1, 784).to(device)
        labels = labels.to(device)

        # optimizer 勾配0にする
        optimizer.zero_grad()

        # 画像入力 -> 推論 まで、この一行だけ!!!
        outputs = net(images)
        
        # outputs とlabelsのロスを計算。
        loss = criterion(outputs, labels)

        # このミニバッチでの、ロスと正確率。
        train_loss += loss.item()
        train_acc += (outputs.max(1)[1] == labels).sum().item()
        
        # 逆伝播の計算・重み更新 
        loss.backward()
        optimizer.step()

    # データセット1周したので、平均ロスと正確率計算。
    avg_train_loss = train_loss / len(train_loader.dataset)
    avg_train_acc = train_acc / len(train_loader.dataset)

    # val=========================================
    # 評価モードへ切り替え
    net.eval()
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.view(-1, 784).to(device)
            labels = labels.to(device)
            outputs = net(images)
            loss = criterion(outputs, labels)
    
            val_loss += loss.item()
            val_acc += (outputs.max(1)[1] == labels).sum().item()
        avg_val_loss = val_loss / len(test_loader.dataset)
        avg_val_acc = val_acc / len(test_loader.dataset)

        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {avg_train_loss:.4f}, val_loss: {avg_val_loss:.4f}, val_acc: {avg_val_acc}')

        train_loss_list.append(avg_train_loss)
        train_acc_list.append(avg_train_acc)
        val_loss_list.append(avg_val_loss)
        val_acc_list.append(avg_val_acc)


# 損失と正確率の変化(折れ線グラフ) を描画
plt.figure()
plt.plot(range(num_epochs), train_loss_list, color='blue', linestyle='-', label='train_loss')
plt.plot(range(num_epochs), val_loss_list, color='green', linestyle='--', label='val_loss')
plt.legend()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.title('Training and validation loss')
plt.grid()

plt.figure()
plt.plot(range(num_epochs), train_acc_list, color='blue', linestyle='-', label='train_acc')
plt.plot(range(num_epochs), val_acc_list, color='green', linestyle='--', label='val_acc')
plt.legend()
plt.xlabel('epoch')
plt.ylabel('acc')
plt.title('Training and validation accuracy')
plt.grid()


