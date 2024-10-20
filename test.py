from z3 import *

# Create real variables
x = Real('x')
y = Real('y')

# Create a solver instance
solver = Solver()

# Add constraints
solver.add(x + 2*y <= 8)
solver.add(3*x + y <= 9)
solver.add(x >= 0)
solver.add(y >= 0)

# Create an optimization problem
opt = Optimize()

# Objective function to maximize
opt.maximize(3*x + 4*y)

# Add the same constraints to the optimizer
opt.add(x + 2*y <= 8)
opt.add(3*x + y <= 9)
opt.add(x >= 0)
opt.add(y >= 0)

# Check for a solution
if opt.check() == sat:
    model = opt.model()
    print(f'Maximum value: {model.eval(3*x + 4*y)}')
    print(f'Solution: x = {model[x]}, y = {model[y]}')
else:
    print('No solution exists.')
