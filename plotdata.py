import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
from matplotlib.animation import FuncAnimation

data = pd.read_csv('MergeData.csv')
temp1 = data['temperature1']
humidity1 = data['humidity1']
flames1 = data['flame1']
temp2 = data['temperature2']
humidity2 = data['humidity2']
flames2 = data['flames2']

plt.style.use('seaborn')
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(temp1, label='Tem D1', color ='red')
ax1.plot(humidity1, label='Hum D1', color ='blue')
ax1.plot(flames1, label='Flames D1', color ='orange')

ax2.plot(temp2, label='Tem D2', color ='red')
ax2.plot(humidity2, label='Hum D2', color ='blue')
ax2.plot(flames2, label='Flame D2', color ='orange')
ax1.legend()
ax2.legend()
plt.tight_layout()
plt.show()




# def animate(i):

#     data = pd.read_csv('MergeData.csv')
#     temp1 = data['temperature1']
#     humidity1 = data['humidity1']
#     flames1 = data['flame1']
#     temp2 = data['temperature2']
#     humidity2 = data['humidity2']
#     flames2 = data['flames2']
#     plt.cla()
#     plt.plot(temp1, label=' temp', color='red' )
#     plt.plot(humidity1, label=' humidity', color ='blue' )
#     plt.plot(flames1, label='flames', color='orange')
#     plt.legend(loc = 'upper right')
# anim = FuncAnimation(plt.gcf(), animate, interval=800)
# plt.tight_layout()
# plt.show()












