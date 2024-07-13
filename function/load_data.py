import pandas as pd


def load_data(city, month, day):
    from bikeshare_2 import CITY_DATA
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week_of_day'] = df['Start Time'].dt.day_name()

    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
       df = df[df['month'] == month]

    if day != "All":
        df = df[df['week_of_day'] == day]

    return df
