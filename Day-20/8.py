import random
import matplotlib.pyplot as plt

random_floats = [random.random() for _ in range(100)]

plt.plot(random_floats, marker='o', linestyle='None')
plt.xlabel("Index")
plt.ylabel("Random Float")
plt.title("Random Floating-Point Numbers")
plt.show()
