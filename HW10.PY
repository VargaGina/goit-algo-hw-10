import pulp

# Define the problem
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Define decision variables
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Define the objective function
problem += lemonade + fruit_juice, "Total_Production"

# Define the constraints
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
problem += 1 * lemonade <= 50, "Sugar"
problem += 1 * lemonade <= 30, "Lemon_Juice"
problem += 2 * fruit_juice <= 40, "Fruit_Puree"

# Solve the problem
problem.solve()

# Print the results
print(f"Optimal number of Lemonade to produce: {pulp.value(lemonade)}")
print(f"Optimal number of Fruit Juice to produce: {pulp.value(fruit_juice)}")
print(f"Maximum total production: {pulp.value(problem.objective)}")


import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Define the function to integrate
def f(x):
    return x ** 2

# Integration bounds
a = 0
b = 2

# Monte Carlo method
def monte_carlo_integration(f, a, b, num_points=10000):
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(0, f(b), num_points)

    sub_curb=y_random<f(x_random)

    estimare_integration=(b-a)*f(b)*np.mean(sub_curb)
    return estimare_integration
    

# Calculate the integral using the Monte Carlo method
mc_result = monte_carlo_integration(f, a, b)
print(f"Monte Carlo Integral Result: {mc_result}")

# Calculate the integral using the quad function
quad_result, error = spi.quad(f, a, b)
print(f"Quad Function Integral Result: {quad_result} with a estimation of error: {error}")


# Plotting the function and the area under the curve
x = np.linspace(- 0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Integration of f(x) = x^2 from {a} to {b}')
plt.grid()
plt.show()
