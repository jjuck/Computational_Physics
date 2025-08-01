import numpy as np
import matplotlib.pyplot as plt

# Define constants
G = 6.67408e-11   # gravitational constant, m^3/kg/s^2
M = 5.972e24      # mass of the Earth, kg
m = 7.342e22      # mass of the Moon, kg
R = 3.844e8       # distance between Earth and Moon, m

# Define the initial conditions
x0 = R           # initial x position of the Moon, m
y0 = 0           # initial y position of the Moon, m
vx0 = 0          # initial x velocity of the Moon, m/s
vy0 = 1022       # initial y velocity of the Moon, m/s

t0 = 0           # initial time, s
t_end = 2.5e6    # end time, s
dt = 1000        # time step, s

# Define the derivative function
def derivs(t, y):
    x, y, vx, vy = y
    r = np.sqrt(x**2 + y**2)
    ax = -G*M*x/r**3 - G*m*(x-R)/r**3
    ay = -G*M*y/r**3 - G*m*y/r**3
    return [vx, vy, ax, ay]

# Initialize arrays to store the solutions
t_arr = np.arange(t0, t_end, dt)
y_arr = np.zeros((len(t_arr), 4))
y_arr[0,:] = [x0, y0, vx0, vy0]

# Implement the RK4 algorithm
for i in range(len(t_arr)-1):
    t = t_arr[i]
    y = y_arr[i,:]
    k1 = dt*np.array(derivs(t, y))
    k2 = dt*np.array(derivs(t+0.5*dt, y+0.5*k1))
    k3 = dt*np.array(derivs(t+0.5*dt, y+0.5*k2))
    k4 = dt*np.array(derivs(t+dt, y+k3))
    y_arr[i+1,:] = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)

# Plot the results
plt.plot(y_arr[:,0], y_arr[:,1])
plt.axis('equal')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Orbit of the Moon around the Earth')
plt.show()
