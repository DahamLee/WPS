import math
import matplotlib.pyplot as plt

x = [n for n in range(1, 31)]
y1 = list(map(lambda n: n, x))
y2 = list(map(lambda n: math.log(n), x))
y3 = list(map(lambda n: n * math.log(n), x))
#y4 = list(map(lambda n : n ** 2, x))

plt.plot(x, y1, label = 'O(n)', color = 'black')
plt.plot(x, y2, label = 'O(log n)', color = 'green')
plt.plot(x, y3, label = 'O(n*log n)', color = 'red' )
#plt.plot(x, y4, label = 'O(n^2)', color = 'purple')

plt.xlabel("n")
plt.ylabel("Big O")
plt.title("Big Os")
plt.legend()
plt.show()
