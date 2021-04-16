import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


def harshaFilter(csv_file, g):
    # reads the  csv file as pandas dataframe
    sensor_data = pd.read_csv(csv_file, header=None)
    x = np.asarray(sensor_data[0])
    y = np.asarray(sensor_data[1])

    # calculating filtered signal by looping through the signal data
    filtered_x = x.copy().tolist()
    filtered_y = y.copy().tolist()
    for i in range(1, len(filtered_y)):
        filtered_y[i] = g*(sum(y[0:i]) - sum(filtered_y[0:i-1]))

    return x, y, filtered_x, filtered_y


# visualisation function
def visualize(x, y, filtered_x, filtered_y, g):
    fig, ax = plt.subplots()
    plt.title(f'Dr.Harsha Filter (g = {g})')
    plt.plot(x, y, label='unfiltered')
    plt.plot(filtered_x, filtered_y, label='filtered')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.show()


g = 0.03
x, y, filtered_x, filtered_y = harshaFilter(
    'sensor_data_with_noise.csv', g)
visualize(x, y, filtered_x, filtered_y, g)
