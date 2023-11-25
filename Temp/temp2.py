import numpy as np
from matplotlib import pyplot as plt
x=np.arange(-10,10,0.05)
y=x**2+5*np.sin(x)
plt.plot(x,y)
plt.xlabel("Truc x")
plt.xlabel("Truc y")
plt.title("Toan cao cap")
plt.show()