import numpy as np
import matplotlib.pyplot as plt

X = np.random.uniform(-1, 4, 30)

def Y(X):
    return 3*X - X**2 + 1

x_val = X[15]
y_val = Y(x_val)
print(f"Значение функции в точке X(i=15): Y({x_val:.2f}) = {y_val:.2f}")

def derivative(X):
    return 3 - 2*X

slope = derivative(x_val)
print(f"Наклон касательной в точке X(i=15): {slope:.2f}")

def tangent_line(X):
    return slope * (X - x_val) + y_val

X_dense = np.linspace(-1, 4, 500)
Y_dense = Y(X_dense)
Y_tangent = tangent_line(X_dense)

plt.plot(X_dense, Y_dense, label="Y(X) = 3X - X^2 + 1", color="blue")
plt.plot(X_dense, Y_tangent, '--', label=f"Касательная в точке X({x_val:.2f})", color="red")

plt.scatter([x_val], [y_val], color="green", zorder=5, label=f"Точка касания X({x_val:.2f})")

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.title("График функции и касательная")

plt.show()
