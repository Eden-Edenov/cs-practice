import numpy as np



hours = np.arange(0, 22, 3)

line = np.linspace(0, 1, 5)

zeros = np.zeros(6, dtype=int)

unknown_table = np.full((2, 3), -1)

identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print()



print("Третий элемент:", hours[2])

print("Элементы с индексами 2-5:", hours[2:6])

print("Каждый второй элемент:", hours[::2])

print("В обратном порядке:", hours[::-1])
print()
