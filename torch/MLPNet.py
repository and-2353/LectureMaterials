import torch
import torchvision
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt

train_dataset = torchvision.datasets.CIFAR10(root='./data/',
                                             train=True,
                                             transform=transforms.ToTensor(),
                                             download=True)