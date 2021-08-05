import torch


n = torch.rand(3)

print('N',n)

check = torch.cuda.is_available()

print('Cuda Available',check)

#lets creatwe an empty tensor

x = torch.empty(3)

x2d = torch.empty(2,3)

print('X is Empty',x)
print('X2d is 2d',x2d)