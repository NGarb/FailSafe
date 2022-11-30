import torch
import numpy as np


def describe(x):
    print("Type: {}".format(x.type()))
    print("Shape/size: {}".format(x.shape))
    print("Values: \n{}".format(x))


if __name__ == "__main__":
    '''describe(torch.Tensor(2, 3))
    describe(torch.rand(2, 3))  # uniform random
    describe(torch.randn(2, 3))  # random normal
    describe(torch.zeros(2, 3))
    x = torch.ones(2, 3)
    describe(x)
    x.fill_(5)
    describe(x)
    x = torch.Tensor([[1, 2, 3],
                      [4, 5, 6]])

    npy = np.random.rand(2, 3)
    describe(torch.from_numpy(npy))
    #page 23 / 210 
    describe(torch.add(x, x))
    describe(x + x)
    describe(x)
    describe(torch.sum(x, dim=0))
    describe(torch.sum(x, dim=1))
    describe(torch.transpose(x, 0, 1))
    x = torch.arange(6).view(2, 3)
    describe(x)
    describe(x[:1, :2])
    indices = torch.LongTensor([0, 2])
    describe(torch.index_select(x, dim=1, index=indices))
    row_indices = torch.arange(2).long()
    col_indices = torch.LongTensor([0, 1])
    describe(x[row_indices, col_indices])
    x = torch.arange(6).view(2, 3)
    describe(x)
    describe(torch.cat([x, x], dim=0))
    describe(torch.cat([x, x], dim=1))
    describe(torch.stack([x, x]))
    x1 = torch.arange(6).view(2, 3)
    describe(x1)
    x2 = torch.ones(3, 2).type(torch.LongTensor)
    x2[:, 1] += 1
    describe(x2)
    describe(torch.mm(x1, x2)) # page 28
    x = torch.ones(2, 2, requires_grad=True)
    describe(x)
    print(x.grad is None)
    x = torch.ones(2, 2, requires_grad=True)
    y = (x + 2) * (x + 5) + 3
    describe(y)
    print(x.grad is None)
    z = y.mean()
    describe(z)
    z.backward()
    print(x.grad is None)
    print(torch.cuda.is_available())'''
    # Exercises
    # 1. Create a 2D tensor and then add a dimension of size 1 inserted at dimension 0.
    example = torch.Tensor(2, 3)
    example = example.unsqueeze(0)
    # 2. Remove the extra dimension you just added to the previous tensor.
    example = example.squeeze()
    # 3. Create a random tensor of shape 5x3 in the interval [3, 7)
    torch.from_numpy(np.random.randint(low=3, high=7, size=(5,3)))
    # 4. Create a tensor with values from a normal distribution (mean=0, std=1).
    torch.randn(3)
    torch.rand(3).normal_()
    # 5. Retrieve the indexes of all the nonzero elements in the tensor torch.Tensor([1, 1, 1, 0, 1]).
    tensor_a = torch.Tensor([1, 1, 1, 0, 1])
    tensor_a[np.where(tensor_a>0)]
    torch.nonzero(tensor_a)
    # 6. Create a random tensor of size (3,1) and then horizontally stack four copies together.
    tensor_b = torch.rand(3,1)
    torch.stack([tensor_b,tensor_b,tensor_b,tensor_b],dim=0)
    tensor_b.expand(3,4)
    # 7. Return the batch matrix­matrix product of two three­dimensional matrices  (a=torch.rand(3,4,5), b=torch.rand(3,5,4)).
    a=torch.rand(3,4,5)
    b = torch.rand(3, 5, 4)
    torch.bmm(a,b)
    # 8. Return the batch matrix­matrix product of a 3D matrix and a 2D matrix (a=torch.rand(3,4,5), b=torch.rand(5,4)).
    a = torch.rand(3, 4, 5)
    b = torch.rand(5, 4)
    torch.bmm(a, b.unsqueeze(0).expand(a.size(0), *b.size()))
    # page 34
    