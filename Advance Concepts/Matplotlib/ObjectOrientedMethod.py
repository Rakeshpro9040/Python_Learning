import os
import matplotlib.pyplot as plt
import numpy as np

os.system('cls')

x = np.linspace(0, 10, 20)
y = x ** 2

# Creates blank canvas
fig = plt.figure(figsize =(3,3) )

axes1 = fig.add_axes([0, 0,1, 1]) # main axes            # left, bottom, width, height (range 0 to 1)
axes2 = fig.add_axes([0.1, 0.5, 0.3, 0.3])# inset axes    # left, bottom, width, height (range 0 to 1)

# axes1 = fig.add_axes([0, 0.5,1, 1]) # main axes            # left, bottom, width, height (range 0 to 1)
# axes2 = fig.add_axes([0, 0 , 0.5, 0.5]) # inset axes    # left, bottom, width, height (range 0 to 1)


# Larger Figure Axes 1
axes1.plot(x, y, 'b')
# axes1.set_xlabel('X_label_axes1')
# axes1.set_ylabel('Y_label_axes1')
# axes1.set_title('Axes 1 Title')

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
# axes2.set_xlabel('X_label_axes2')
# axes2.set_ylabel('Y_label_axes2')
# axes2.set_title('Axes 2 Title')

# fig.tight_layout(); Not applicable
plt.show()