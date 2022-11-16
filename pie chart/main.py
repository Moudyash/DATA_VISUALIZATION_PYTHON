import matplotlib.pyplot as plt
import pandas as pd


def first():
    # Data to plot consists of  labels, sizes and colors for each # label
    labels = 'Python', 'C++', 'Ruby', 'Java'
    sizes = [215, 130, 245, 210]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels,
            colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)

    plt.axis('equal')
    plt.title("pie chart")
    # Adding legend

    plt.legend()#to show small squre contain the data
    plt.legend(title="programing languages:")

    plt.show()


def second():
    # Data to plot consists of  labels, sizes and colors for each # label
    labels = 'Python', 'C++', 'Ruby', 'Java'
    sizes = [215, 130, 245, 210]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    # Plot
    patches, texts = plt.pie(sizes, colors=colors, shadow=True,
                             startangle=90)

    plt.legend(patches, labels, loc="best")
    plt.axis('equal')

    plt.show()


first()
