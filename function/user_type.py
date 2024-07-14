
import time


def user_stats(df):
    stats = {}
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    stats['user_types'] = df['User Type'].value_counts().to_dict()

    # Display counts of gender
    if 'Gender' in df:
        stats['gender_counts']= df['Gender'].value_counts().to_dict()

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        stats['earliest_year'] = int(df['Birth Year'].min())
        stats['most_recent_year'] = int(df['Birth Year'].max())
        stats['common_year'] = int(df['Birth Year'].mode()[0])
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return stats
