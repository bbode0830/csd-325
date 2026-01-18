"""
Ben Bode
1/18/2026
module 4.2 assignment
code modified from code in sitka_weather.zip accessed from class webpage
"""

import csv
from datetime import datetime
from matplotlib import pyplot as plt




# initialize the path value
path = input("This program prints a graph of the highest or lowest recorded temperature for each day in 2018."
      " Enter 'H' to see highs, 'L' to see lows, or 'E' to exit.")

# If the user wants to see the high temperatures:
while path.lower() == 'h':

    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        # Get dates and high temperatures from this file.
        dates, highs = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)

    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
        
    # check what the user wants to do next
    path = input("Enter 'H' to see the highs, 'L' to see the lows, or 'E' to exit.")

# If the user wants to see the low temperatures:
while path.lower() == 'l':

    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        # Get dates and low temperatures from this file.
        dates, lows = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            low = int(row[6])
            lows.append(low)

    # Plot the low temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    # Format plot.
    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

    # check what the user wants to do next
    path = input("Enter 'H' to see the highs, 'L' to see the lows, or 'E' to exit.")

# handle any other inputs
while path.lower() not in ('l', 'h', 'e'):

    path = input("You did not enter a vaild input. Please enter 'H' for highs, 'L' for lows, or 'E' to exit.")

# if the user wants to exit the program
if path.lower() == 'e':

    print("Thank you for using the program!")