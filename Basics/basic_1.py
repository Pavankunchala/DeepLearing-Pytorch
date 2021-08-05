import torch


n = torch.rand(3)

print('N',n)

check = torch.cuda.is_available()

print('Cuda Available',check)

#lets creatwe an empty tensor

x = torch.empty(3)

print('X is Empty',x)