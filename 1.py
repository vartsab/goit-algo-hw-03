from datetime import datetime as dt

def get_days_from_today(date):
    delta = dt.today() - dt.strptime(date, "%Y-%m-%d")
    return delta.days

print(get_days_from_today("2024-04-22"))