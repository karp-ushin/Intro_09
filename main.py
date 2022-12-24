import matplotlib.pyplot as plt

function = input('Enter f(x) : ')
with open('f.py', "w") as file_handler:
    file_handler.write('from math import *\n\n\n')
    file_handler.write('def f(x):\n    return ')
    file_handler.write(function)
    file_handler.write('\n')

from f import f

X = [i*0.1 for i in range(-100, 100)]
Y = [f(x) for x in X]
plt.plot(X, Y)
plt.ylabel(function)
plt.show()
