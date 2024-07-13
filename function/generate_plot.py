import os
from matplotlib import pyplot as plt


def generate_plot(df):
    plt.figure()
    df['Start Time'].dt.hour.hist(bins=24)
    plt.title('Distribution of Start Times')
    plt.xlabel('Hour of Day')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plot_path = os.path.join('static', 'plot.png')
    plt.savefig(plot_path)
    plt.close()
    return plot_path
