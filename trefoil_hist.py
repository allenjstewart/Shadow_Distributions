import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
outcomes = ('1', '2', '3')
y_pos = np.arange(len(outcomes))
dist = [3,4,1]
 
plt.bar(y_pos, dist, align='center', alpha=0.5)
plt.xticks(y_pos, outcomes)
plt.ylabel('Number of components')
plt.title('Number of outcomes')
 
plt.show()