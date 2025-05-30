import numpy as np
from matplotlib import pyplot as plt
import matplotlib
names = ['ns125','ns160','hornet','ns200','mt15']
arr  = [107693,139168,143451,152237,175889]
price_diff = []
percent_diff = []
def plot_orginal_data(arr):
    plt.plot(names, arr, marker='o')
    plt.title('Original Data')
    plt.xlabel('Names')
    plt.ylabel('Values')
    plt.grid()
    plt.show()
def calculate_price_diff(arr):
    for i in range(len(arr)):
        price_ =[]
        for j in range(0, len(arr)):
            diff =  abs(arr[j] - arr[i])
            price_.append(diff)
        plot_orginal_data(price_)
        price_diff.append(price_)
    return price_diff
print(calculate_price_diff(arr))


# plot_orginal_data(arr)
def plot_percent_diff(percent_diff):
    plt.plot(names, percent_diff, marker='o')
    plt.title('Percent Difference')
    plt.xlabel('Names')
    plt.ylabel('Percent Difference')
    plt.grid()
    plt.show()
def calculate_percent_diff(arr):
    for i in range(len(arr)):
        percent_ = []
        for j in range(0, len(arr)):
            diff = abs(arr[j] - arr[i]) / arr[i] * 100
            percent_.append(diff)
        # plot_percent_diff(percent_)
        percent_diff.append(percent_)
    return percent_diff
print(calculate_percent_diff(arr))

# plot_percent_diff(arr)