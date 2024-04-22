from datetime import datetime as dt, timedelta as td

def get_upcoming_birthdays(users: list) -> list:
    # Declare a resulting list
    congratulation_date=[]
    # Store the current date and 7 days from now
    today = dt.today().date()
    seven_days_from_now = today + td(days=7)

    for user in users:
            # Find the next celebration date for each entry
            dob = dt.strptime(user["birthday"], "%Y.%m.%d").date()
            next_celebration_date = dob.replace(year=today.year)
            # If the birthday have already passed this year, next celebration is in the following year
            if next_celebration_date < today:
                next_celebration_date = dob.replace(year=today.year + 1)
            # Checking if the next celebration date is within the next 7 days
            if next_celebration_date < seven_days_from_now:
                # If the celebration date falls on Sat(5) or Sun(6) celebration date should be on the following Monday
                if next_celebration_date.weekday() in [5,6]:
                    next_celebration_date += td(days=(7-next_celebration_date.weekday()))
                # Appending the new entry to the resulting list
                congratulation_date.append({"name": user["name"], "congratulation_date": dt.strftime(next_celebration_date, "%Y.%m.%d")})

    return congratulation_date

users = [
        {"name": "Ivan Vasylovych", "birthday" : "1996.06.28"}, 
        {"name": "Petro Sergiiovych", "birthday" : "2001.04.28"},
        {"name": "Olena Vitaliivna", "birthday" : "1969.04.20"},
        {"name": "Darka Panteliivna", "birthday" : "2004.11.22"}
        ]
print(get_upcoming_birthdays(users))