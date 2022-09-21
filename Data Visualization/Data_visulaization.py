# Popular plotting libraries in python

# Matplotlib - It is used to create two dimensional graphs and plots
# Pandas visualization - It is easy to use interface and built on matplotlib
# Seaborn - It provides a high level interface for drawing attractive and informative statisticla graphics
# GG_plot -  It is based o R language's GG plot
# Plotly - It can create interactive plot

import os
import pandas as pd
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

plt.title('Weather')
plt.xlabel('Day')
plt.ylabel('Temperature')

plt.plot(x,y,'ro')
plt.plot(x,y,color='green',linewidth=4, linestyle = 'dotted')
plt.plot(x,y, '--' )
plt.show()

# SCATTER PLOT -

plt.scatter(x, y, color='green')
plt.show()

# HISTOGRAM -
# Histogram is used to represnt frequency distribution of numerical values -

plt.hist(x,y)
plt.show()