import random as rn

def get_numbers_ticket(min, max, quantity):
    if (min < 1) or (max < min) or (max > 1000) or ((max - min - quantity) < -1):
        return "Не вірно задані вхідні параметри лотереї!\n" \
               "Будь-ласка впевніться, що 0 < min < max < 1000."
    res=set()
    while len(res) < quantity:
        res.add(rn.randint(min,max))
    return res

print(get_numbers_ticket(1,6,6))