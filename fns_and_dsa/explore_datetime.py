#This script demonstrates ability to use datetime module for handling date and time

from datetime import datetime, timedelta
#Part 1: Display current Date and time

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S") #Format the date
    print(f"Current date and time: {formatted_date}")

#Part 2: Calculate a Future Date
def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days_to_add) #Add days to current date
    formatted_future_date = future_date.strftime("%Y-%m-%d") #Format future date
    print(f"Future date: {formatted_future_date}")

#Part 3: Main execution
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
