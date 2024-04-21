from datetime import datetime as dt

def get_days_from_today(date):
    try:
        # Trying to parse the input into datettime object
        # and find the difference with todays date.
        delta = dt.today() - dt.strptime(date, "%Y-%m-%d")
        return delta.days
    except ValueError:
        # The wrong input format will cause ValueError
        return "Invalid input! The input must follow the pattern YYYY-MM-DD"

print(get_days_from_today("2024-04-22"))