from colorama import init, Fore, Back, Style
from google_currency import convert
init()

conv = input('Хотите конвертировать валюту? (да или нет) ').lower()

while conv.startswith('д') or conv.startswith('l'):
    amount = input('Сколько денег будем переводить? ')
    try:
        amount = float(amount)
    except:
        print('Пожалуйста, введите число!')
        conv = input('Хотите конвертировать валюту? (да или нет) ').lower()

    first = input('Из какой валюты будем переводить? ').upper()
    second = input('В какую валюту будем переводить? ').upper()

    print(convert(first,second, amount))


