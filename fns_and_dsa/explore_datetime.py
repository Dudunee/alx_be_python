from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print("Current Date and Time:", formatted_date)
    
    return current_date

def calculate_future_date(days):
    current_date = display_current_datetime()
    
    future_date = current_date + timedelta(days=days)
    
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    print("Future Date after", days, "days:", formatted_future_date)
    
    return future_date

display_current_datetime()

days = int(input("Enter number of days to add: "))
calculate_future_date(days)
