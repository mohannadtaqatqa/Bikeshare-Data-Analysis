
import time


def station_stats(df):
    stats = {}
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
   # display most commonly used start station
    stats['common_start_station'] = df['Start Station'].mode()[0]
    # display most commonly used end station
    stats['common_end_station'] = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    df['Start-End Combination'] = df['Start Station'] + " to " + df['End Station']
    stats['common_trip'] = df['Start-End Combination'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return stats
