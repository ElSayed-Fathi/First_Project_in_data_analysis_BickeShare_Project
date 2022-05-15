#!/usr/bin/env python
# coding: utf-8

# In[18]:


import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # get input from user for city (chicago, new york city, washington). Use a while loop to handle invalid inputs

    while True:
        city_2 = input("\n Would You Like To See Data For chicago , new york city , or washington ? \n").title()
        if city_2 not in ('New York City', 'Chicago', 'Washington'):
            print("Sorry, I didn't catch that. Try again.")
            continue
        else:
            break

    #  get input from user for month (all, january, february, ... , june)

    while True:
        month_2 = input("\n Which Month Would You Like To Filter By ?  january , february , march , april , may ,june,or all ? \n")
        if month_2 not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Sorry, I didn't catch that. Try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day_2 = input("\n Which Day Would You Like To Filter By ?  sunday , monday , tuesday , thursday , wednesday ,friday, saturday or all ?")
        if day_2 not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("Sorry, I didn't catch that. Try again.")
            continue
        else:
            break

    print('-' * 40)
    return city_2, month_2, day_2

#=======================================================================================================================
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

#=======================================================================================================================
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month_11 = df['month'].mode()[0]
    print('Most Common Month:', popular_month_11)

    # TO DO: display the most common day of week

    popular_day_11 = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day_11)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour_11 = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour_11)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

#=======================================================================================================================
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station_11 = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station_11)

    # TO DO: display most commonly used end station

    End_Station_11 = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station_11)

    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station_11, " & ",
          End_Station_11)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

#=======================================================================================================================
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time_11 = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time_11 / 86400, " Days")

    # TO DO: display mean travel time

    Mean_Travel_Time_11 = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time_11 / 60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

#=======================================================================================================================
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types_11 = df['User Type'].value_counts()

    print('User Types:\n', user_types_11)

    # TO DO: Display counts of gender

    try:
        gender_types_11 = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types_11)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        Earliest_Year_11 = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year_11)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")

    try:
        Most_Recent_Year_11 = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year_11)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")

    try:
        Most_Common_Year_11 = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Most_Common_Year_11)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



 #======================================================================================================================
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    keep_asking = True
    while (keep_asking):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == "no": 
            keep_asking = False   

#=======================================================================================================================
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()











