import matplotlib.pyplot as plt

x = [i for i in range(200)]
y = [e**2 for e in x]


plt.plot(x,y)
plt.savefig('gg.png')
plt.show()