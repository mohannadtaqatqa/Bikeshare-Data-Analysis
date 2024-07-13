def time_stats(df):
    stats = {}
    # display the most common month
    month = df['Start Time'].dt.month
    stats['most_common_month'] = month.mode()[0]
    
    # display the most common day of week
    day = df['Start Time'].dt.day_name()
    stats['most_common_day'] = day.mode()[0]

    # display the most common start hour
    hour = df['Start Time'].dt.hour
    stats['most_common_hour'] = hour.mode()[0]
    return stats
