
import time


def trip_duration_stats(df):
    stats = {}
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    stats['total_duration'] = df['Trip Duration'].sum()


    # display mean travel time

    stats['average_duration'] = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    return stats
