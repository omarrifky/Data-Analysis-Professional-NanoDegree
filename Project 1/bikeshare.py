import time
import pandas as pd
import numpy as np
import calendar 
import datetime 
from datetime import date
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyorkcity': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'all':13}
days = {'sunday':6,'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'all':8}
filteroptions = ['month','day','both','none']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! If you wish to exit at any time enter exit')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True: # Keep Taking input from the user until the user enters a valid city
        try:
            city = input("Which city would you like to see data for? Chicago , New York City or Washington:")
            city = city.lower();
            city = city.replace(" ", "")
            if city=="exit":
                print("Exiting now")
                return 'exit','exit','exit'
            if CITY_DATA.get(city) is not None:
                break;
            else:
                print('Please enter a city from the options above:')
        except KeyboardInterrupt:
            print("Oops!", sys.exc_info()[0], "occurred")

    
   
    
    month = "none" # default value for month is none
    day = "none"# default value for day is none
    filteroption = "none"
   

    while True and city!='exit': # Keep Taking input from the user until the user enters a valid filter option
        try:
            filteroption = input("Would you like to filter by month, day or both? Enter none if no time filter is needed:")
            filteroption = filteroption.lower();
            filteroption = filteroption.replace(" ", "")
            if filteroption =='exit':
                print("Exiting now")
                return 'exit','exit','exit'
            if filteroption in filteroptions :
                break;
            else:
                print('Please enter a one from the options above months,days,both, none:')
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")


 # get user input for month (all, january, february, ... , june)
    while True and (filteroption=='both' or filteroption =='month') and (city!='exit'and filteroption!='exit'): # Keep Taking input from the user until the user enters a valid month
        try:
            month = input("Which month?January,February,March,April,May,June or enter all if all needed:")
            month = month.lower();
            month = month.replace(" ","")
            if month =='exit':
                print("Exiting now")
                return 'exit','exit','exit'
            if months.get(month) is not None:
                break;
            else:
                print('Please enter one of the options above')
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True and (filteroption=='both'or filteroption == 'day') and (city!='exit' and filteroption!='exit' and month!='exit' ):# Keep Taking input from the user until the user enters a valid day
        try:
            day = input("Which Day? Please enter one of Sunday,Monday,Tuesday,Wednesday,Thursday,Friday Saturday or enter all if all needed:")
            day = day.lower();
            day = day.replace(" ", "")
            if day=='exit':
                print("Exiting now")
                return 'exit','exit','exit'
            if day in days:
                break;
            else:
                print('Please enter one of the options above')
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")

    
   

    print('-'*40)
    return city, month, day


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
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
  
    if month != 'all' and month!='none':
        df = df[df['Start Time'].dt.month == months.get(month)]
        df = df[df['End Time'].dt.month == months.get(month)]
    
    
    if day !='all' and day!='none':
        df = df[df['Start Time'].dt.dayofweek==days.get(day)]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = (df['Start Time'].dt.month).value_counts().idxmax() #idxmax returns index of the max count

    print("Most Common month is: " , most_common_month)

    # display the most common day of week
    most_common_day = (df['Start Time'].dt.dayofweek).value_counts().idxmax()
    
    for name, daynum in days.items(): 
        if daynum == most_common_day:
            most_common_day = name 
            break
    print("Most Common day is: " , most_common_day)

    # display the most common start hour
    most_common_hour = (df['Start Time'].dt.hour).value_counts().idxmax()
    print("Most Common hour is: " , most_common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df): #CHECK
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    most_common_start_station = (df['Start Station']).value_counts().idxmax() 
    print("Most Common Start Station is: " , most_common_start_station)

    # display most commonly used end station
    most_common_end_station = (df['End Station']).value_counts().idxmax() 
    print("Most Common End Station is: " , most_common_end_station)


    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0] 
  #  most_common_start_end_station =  (df['Start Station'] + df['End Station']).mode()[0]
   
    print("Most Common Start and End Station combined, Start Station is ",most_common_start_end_station[0]+", End Station is ",most_common_start_end_station[1])
   # print("Most Common Start and End Station combined, Start Station is ",most_common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is: ", mean_travel_time)


    # display max travel time
    max_travel_time = df['Trip Duration'].max()
    print("Maximum travel time is: ", max_travel_time)
    
    
    # display min travel time
    min_travel_time = df['Trip Duration'].min()
    print("Minimum travel time is: ", min_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_birth(df):
    print('\nCalculating User birth Stats...\n')
    start_time = time.time()
    most_common_birth_year = (df['Birth Year']).value_counts().idxmax() 
    print("Most common birth year is :",int(most_common_birth_year))
    
    earliest_birth_year = (df['Birth Year']).min()
    print("Earliest birth year is :",int(earliest_birth_year))
    
    most_recent_birth_year = (df['Birth Year']).max()
    print("Most recent birth year is :",int(most_recent_birth_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def gender_stats(df):
    print('\nCalculating Gender Stats...\n')
    start_time = time.time()
    
    gender_counts = df['Gender'].count()
    print("Gender counts is :",gender_counts)
    
    male_count = df[df['Gender'] == 'Male'].count()[0]
    print("Male count is :",male_count)
    
    female_count =  df[df['Gender'] == 'Female'].count()[0]
    print("Female count is :",female_count)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (True):
        print(df.iloc[start_loc:start_loc+5])
        
        start_loc += 5
        try:
            view_data = input("Do you wish to continue?: ").lower()
            if(view_data=='no'):
                break;
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")

            
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df['User Type'].value_counts()[0]
    print("User types count is :",user_counts)
  
    # Display earliest, most recent, and most common year of birth
    most_common_year = (df['Start Time'].dt.year).value_counts().idxmax() 
    print("Most common year is :",most_common_year)
    earliest_year = (df['Start Time'].dt.year).min()
    print("Earliest year is :",earliest_year)
    most_recent_year = (df['Start Time'].dt.year).max()
    print("Most recent year is :",most_recent_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        if city=='exit' or 'month'=='exit' or day =='exit':
            break;
        df = load_data(city, month, day)
        print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        if 'Birth Year' in df.columns:
            user_birth(df)
        if 'Gender' in df.columns:
            gender_stats(df)
        display_data(df)
        try:    
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")


if __name__ == "__main__":
	main()
