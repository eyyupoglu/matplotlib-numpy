import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import the matplotlib.pyplot module

x = (1, 3, 4, 5) # Make some data, x- and y-values
y = (2, 3, 3, 4)
#---------------------------LINE-PLOT---------------------------------------------------------
plt.plot(x, y)
plt.title("Simple line graph")

plt.xlabel("x-values") # Set the x-axis label
plt.ylabel("y-values") # Set the y-axis label

plt.xlim([0, 6]) # Set the limits of the x-axis
plt.ylim([0, 5]) # Set the limits of the y-axis
plt.show()
#---------------------------SCATTER-PLOT--------------------------------------------------------
plt.plot(x, y, "b*")
plt.title("Simple scatter plot") # Set the title of the graph
plt.xlabel("x-values") # Set the x-axis label
plt.ylabel("y-values") # Set the y-axis label
plt.xlim([0, 6]) # Set the limits of the x-axis
plt.ylim([0, 5]) # Set the limits of the y-axis
plt.show()
#---------------------------GRID-RED-LINE-RED SCATTER---------------------------------------------------------
plt.plot(x, y, '*r-')
plt.title("Simple scatter plot") # Set the title of the graph
plt.xlabel("x-values") # Set the x-axis label
plt.ylabel("y-values") # Set the y-axis label
plt.xlim([0, 6]) # Set the limits of the x-axis
plt.ylim([0, 5]) # Set the limits of the y-axis
plt.grid()
plt.show()
#-----------------------------RED-POINTS-------------------------------------------------------
plt.plot(x, y, 'ro')
plt.title("Simple scatter plot") # Set the title of the graph
plt.xlabel("x-values") # Set the x-axis label
plt.ylabel("y-values") # Set the y-axis label
plt.xlim([0, 6]) # Set the limits of the x-axis
plt.ylim([0, 5]) # Set the limits of the y-axis
plt.grid()
plt.show()
#-----------------------------red dashes blue squares green triangles-------------------------------------------------------
plt.plot(x, y, 'r--', x, y, 'bs', x, x, 'g^')
plt.title("Simple scatter plot") # Set the title of the graph
plt.xlabel("x-values") # Set the x-axis label
plt.ylabel("y-values") # Set the y-axis label
plt.xlim([0, 6]) # Set the limits of the x-axis
plt.ylim([0, 5]) # Set the limits of the y-axis
plt.grid()
plt.show()
