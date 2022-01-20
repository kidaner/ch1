import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn')

mpl.rcParams['font.family'] = 'serif'

np.random.seed(1000)

y = np.random.standard_normal(20)

x = np.arange(len(y))

plt.plot(y.cumsum())
plt.grid(False)
plt.axis('image')
plt.show()
