import matplotlib.pyplot as plt
import time
import pandas as pd
import numpy as np
import json
from matplotlib.animation import FuncAnimation
from sklearn.linear_model import LogisticRegression
import csv

plt.style.use('seaborn')

def animate(i):

    data = pd.read_csv('MergeData.csv')
    temp1 = data['temperature1']
    humidity1 = data['humidity1']
    flames1 = data['flame1']
    temp2 = data['temperature2']
    humidity2 = data['humidity2']
    flames2 = data['flames2']
    plt.cla()
    plt.plot(temp1, label=' temp', color='red' )
    plt.plot(humidity1, label=' humidity', color ='blue' )
    plt.plot(flames1, label='flames', color='orange')
    plt.legend(loc = 'upper left')
anim = FuncAnimation(plt.gcf(), animate, interval=800)
plt.tight_layout()
plt.show()

