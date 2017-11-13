import numpy as np
import matplotlib.pyplot as plt # Import the matplotlib.pyplot module
import math

x=np.random.uniform(-10, 10, 2000)
y=np.random.uniform(-10, 10, 2000)



print(x)
print(y)
new_x=np.array([])
new_y=np.array([])
for i in range(len(x)):
    if max(np.absolute(x[i]),np.absolute(y[i]))>5 and math.sqrt(x[i]**2 +y[i]**2)<10 :
        new_x=np.append(new_x,x[i])
        new_y=np.append(new_y,y[i])

plt.plot(new_x,new_y,"b*")
plt.title("Simple scatter plot") # Set the title of the graph
plt.xlabel("x-values") # Set the x-axis label
plt.ylabel("y-values") # Set the y-axis label
plt.xlim([-15, 15]) # Set the limits of the x-axis
plt.ylim([-15,+15]) # Set the limits of the y-axis
plt.show()