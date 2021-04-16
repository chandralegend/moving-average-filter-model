import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


def movingAverageFilter(csv_file, window_size):
    # reads the  csv file as pandas dataframe
    sensor_data = pd.read_csv(csv_file, header=None)
    x = np.asarray(sensor_data[0])
    y = np.asarray(sensor_data[1])

    # calculating the cumulative sum of the sensor data
    cumsum = np.cumsum(np.insert(y, 0, 0))

    # caclulating the filtered signal
    filtered_y = (cumsum[window_size:] -
                  cumsum[:-window_size]) / float(window_size)
    filtered_x = x[window_size-1:]

    return x, y, filtered_x, filtered_y


# visualisation function
def visualize(x, y, filtered_x, filtered_y, window_size):
    fig, ax = plt.subplots()
    plt.title(f'Moving Average Filter (window size = {window_size})')
    plt.plot(x, y, label='unfiltered')
    plt.plot(filtered_x, filtered_y, label='filtered')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.show()


window_size = 100
x, y, filtered_x, filtered_y = movingAverageFilter(
    'sensor_data_with_noise.csv', window_size)
visualize(x, y, filtered_x, filtered_y, window_size)
