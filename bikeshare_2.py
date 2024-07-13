from matplotlib import pyplot as plt
import matplotlib

from function.generate_plot import generate_plot
from function.load_data import load_data
from function.station_state import station_stats
from function.time_status import time_stats
from function.trip_dura_status import trip_duration_stats
from function.user_type import user_stats
matplotlib.use('Agg')
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        city = request.form['city'].lower()
        month = request.form['month'].lower()
        day = request.form['day'].title()

        df = load_data(city, month, day)

        stats = {
            **time_stats(df),
            **station_stats(df),
            **trip_duration_stats(df),
            **user_stats(df)
        }
        print(stats)
        plot_path = generate_plot(df)
        plot_url = 'static/plot.png'

        return render_template('index.html', stats=stats,plot_url=plot_url)
    return render_template('index.html')

@app.route('/static/<path:filename>')
def send_file(filename):
    return send_from_directory('static', filename)


if __name__ == "__main__":
    app.run(debug=True)

