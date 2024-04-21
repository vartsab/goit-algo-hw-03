import random as rn

def get_numbers_ticket(min, max, quantity):
    #Перевірка валідності вводу
    if (min < 1) or (max < min) or (max > 1000) or ((max - min - quantity) < -1):
        return "Не вірно задані вхідні параметри лотереї!\n" \
               "Будь-ласка впевніться, що 0 < min < max < 1000."
    #Декларую множину res для зберігання лише унікальних даних
    res = set()
    #Генерую випадкові числа та додаю їх множини допоки список
    #не буде мати потрібну довжину
    while len(res) < quantity:
        res.add(rn.randint(min,max))
    #Повертаю результат роботи функції у вигляді відсортованого списка
    return sorted (res)

print(get_numbers_ticket(1,6,6))