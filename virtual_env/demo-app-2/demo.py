# We import pyplot module from matplotlib packet
# for simplify the methods call we rename it plt
import matplotlib.pyplot as plt
# We import numpy and rename it np
import numpy as np

# We call methode to draw figures
plt.figure()

# Se set the datas to draw
plt.plot([1, 2, 3, 4, 5],[10, 20, 30, 40, 50])

# We display the figure
plt.show()