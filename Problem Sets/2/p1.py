import math
import matplotlib.pyplot as plt

fy = 50
E = 29000
increment = 1

x = []
y = []
euler_x = []
euler_y = []

# Initial values
fcr = fy / 3
klr = math.sqrt(3 * math.pi**2 * E / fy)
x.append(klr)
y.append(fcr)
euler_x.append(klr)
euler_y.append(fcr)

x.append(75.66)
y.append(33.33)

x.append(26.75)
y.append(33.33)

#x.append(53.5)
#y.append(fy)

x.append(18.91)
y.append(fy)

additional_x = []
additional_y = []

additional_x.append(75.66)
additional_y.append(33.33)

additional_x.append(53.5)
additional_y.append(fy)

additional_x.append(18.91)
additional_y.append(fy)

# For euler
fcr = fy / 3
klr = math.sqrt(3 * math.pi**2 * E / fy)
while fcr < fy:
    fcr += 1
    klr = math.sqrt(math.pi**2 * E / (fcr))
    euler_x.append(klr)
    euler_y.append(fcr)

# Plot
plt.title("COLUMN STRENGTH CURVE USING TANGENT MODULUS")
plt.xlabel(r"$\dfrac{K \cdot L}{r}$")
plt.ylabel(r"$F_{cr}$")

tangent, = plt.plot(x, y, label='Tangent Modulus')
euler, = plt.plot(euler_x, euler_y, label='Euler')
plt.legend(handles=[tangent, euler], loc='best', fontsize=14)
plt.plot(additional_x, additional_y, ':')

plt.grid()
plt.show()