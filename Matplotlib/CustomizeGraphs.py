import os
import matplotlib.pyplot as plt
import numpy as np

os.system('cls')

x = np.linspace(0, 10, 20)
y = x ** 2

# Rotating the x-axis and y-axis labels.
plt.plot(x, y, 'r') 
plt.xlabel('X Axis Name') 
plt.ylabel('Y Axis Name') 
plt.title('Graph title') 

plt.xticks([0.5,1.5,2.5] ,rotation = 45 ,color = 'green' , size = 20 , alpha = 0.3) 
#  The list in starting mentions the numbers we want on x-axis  , only the no. in list will be shown on x-axis
# this rotates the points on x-axis by 45 degree and colur is green.

plt.yticks(rotation = 45 , color = 'violet' , size = 20)  

plt.ylim([3,15]) # sets the renge for y axis numbers

plt.grid(True , color='k', linestyle='--', linewidth=2 , alpha = 0.3)  #alpha gives transparency
plt.show() 