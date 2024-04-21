import re

def phone_number (numbers):
    # Declare an empty list to append the results to it
    numbers_sanitized = []
    for number in numbers:
        # Sanitize the number by deleting all extra
        # symbols but digits and "+"
        number = re.sub(r"\D","",number)
        # Check if the number has "+" in it and when not
        # take "+38" and add the last 9 digits of the number
        if not number.startswith("+"):
            number = "+380" + number[-9:]
        #save the entry to the resulting list
        numbers_sanitized.append(number)
    return numbers_sanitized

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

print(phone_number(raw_numbers))