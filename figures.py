import datafilters as df
import matplotlib.pyplot as plt
import numpy as np


def fish():
    labels, values = df.sizeFish()
    fig1, ax1 = plt.subplots(figsize=(10, 4.2))
    ax1.pie(values, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=0)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')
    plt.title('Size of Angler Fish in New Zealand waters (millimeters)')
    return plt.gcf()

def line_plot():   
    labels, values = df.fishAmountYear()
    fig1, ax1 = plt.subplots(figsize=(10, 4.2))
    plt.plot(labels, values)
    print(labels,values)
    return plt.gcf()


def scatter_plots():

    x = np.arange(0, 11)

    y1 = np.random.randint(2, 7, (11,))
    y2 = np.random.randint(9, 14, (11,))
    y3 = np.random.randint(15, 25, (11,))


    plt.scatter(x, y1)
    # plt.scatter(x, y2, marker='v', color='r')
    # plt.scatter(x, y3, marker='^', color='m')
    plt.title('Scatter Plot Example')
    #plt.show()
    return plt.gcf()
