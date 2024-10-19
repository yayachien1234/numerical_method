#!/usr/bin/env python
# coding: utf-8

# In[63]:


import numpy as np
import matplotlib.pyplot as plt
def my_central_diff(y, h):
    s = y.copy()
    for i in range(1, len(y)-1):
        s[i] = (y[i+1]-y[i-1])/(2*h)
    return s
    pass
# step size
h = 0.1
# define grid
x = np.arange(0, 2*np.pi, h)
# compute function
y = np.sin(x)
# compute vector of forward differences
central_diff = my_central_diff(y, h)
central_diff = central_diff[:-1]

# compute corresponding grid
x_diff = x[:-1]
# compute exact solution
exact_solution = np.cos(x_diff)
central_diff[0] = exact_solution[0]

# Plot solution
plt.figure(figsize = (12, 8))
plt.plot(x_diff, central_diff, "-", label = "Finite difference approximation", lw=8)
plt.plot(x_diff, exact_solution, label = "Exact solution", lw=4)
plt.legend()
plt.show()

# Compute max error between
# numerical derivative and exact solution
max_error = max(abs(exact_solution - central_diff))
print('The maximum error is', max_error)


# ### ---Bonus---

# In[ ]:


# define step size
h = 1
# define number of iterations to perform
iterations = 15
# list to store our step sizes
step_size = []
# list to store max error for each step size
max_error = []

for i in range(iterations):
    # halve the step size
    h /= 2
    # ...to be continued

# produce log-log plot of max error versus step size
plt.figure(figsize = (12, 8))
plt.loglog(step_size, max_error, "v", markersize=14)
plt.xlabel('step size', fontsize=20)
plt.ylabel('max error', fontsize=20)
plt.show()


# In[65]:


# define step size
h = 1
# define number of iterations to perform
iterations = 15
# list to store our step sizes
step_size = [] 
# list to store max error for each step size
max_error = [] 

for i in range(iterations):
    # halve the step size
    h /= 2 
    # store this step size
    step_size.append(h) 
    # compute new grid
    x = np.arange(0, 2 * np.pi, h) 
    # compute function value at grid
    y = np.sin(x) 
    # compute vector of forward differences
    central_diff = my_central_diff(y, h)
    # 控制central_diff數量
    central_diff = central_diff[:-1]
    # compute  grid
    # 控制x_diff數量
    x_diff = x[:-1] 
    # compute exact solution
    exact_solution = np.cos(x_diff)
    #補齊少的位數
    central_diff[0] = exact_solution[0]
    
    # Compute max error 
    max_error.append(            max(abs(exact_solution - central_diff)))

# produce plot of max error &step size
plt.figure(figsize = (12, 8))
plt.loglog(step_size, max_error, "v", markersize=14)
plt.xlabel('step size', fontsize=20)
plt.ylabel('max error', fontsize=20)
plt.show()


# In[ ]:




