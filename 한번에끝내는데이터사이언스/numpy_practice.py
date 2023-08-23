import numpy as np

print(np.arange(10))
print(np.arange(10,100))

arr = np.array([1,2,3,4,5])
arr2 = np.array([[1,2],[3,4]])

print(arr.shape)
print(arr2.shape)

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)

print(np.arange(1,10).reshape(3,3))

print(np.arange(6).reshape(6,1))

print(np.arange(6).reshape(-1,1))

print(x)
print(x.reshape(-1))
y = np.arange(10)
print(y.reshape(2,-1))
print(y.reshape(-1,2))

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1+arr2)
print(np.concatenate([arr1, arr2]))

print(np.vstack([arr1, arr2]))
print(np.hstack([arr1, arr2]))

print([1,2,3]*2)
# print([1,2,3]*[2,2,2])  # not working
print(np.array([1,2,3,4,5])*np.array([2,2,2,2,2]))
print(np.array([1,2,3,4,5])*2)

# universal function
f = lambda x: 1/x
print(f(3))
print(type(arr1))
print([f(i) for i in arr1])
print(f(arr1))

# numpy method
mat1 = np.random.randn(5,3)
print(mat1)

print(np.abs(mat1))
print(np.square(mat1))
print(np.sqrt(np.square(mat1)))

vec = np.array([1,2,3,4,5])
print(np.linalg.norm(vec))
mat = np.arange(4).reshape(2,2)
print(np.linalg.eig(mat)) # 아이겐 벡터

print(np.random.rand(100))

import matplotlib.pyplot as plt

plt.scatter(np.arange(100), np.random.rand(100))
plt.show()

plt.scatter(np.arange(100), np.random.randn(100))
plt.show()