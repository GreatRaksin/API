from colorama import init, Fore, Back, Style
from google_currency import convert
init()

conv = input(Fore.BLUE + 'Хотите конвертировать валюту? (да или нет) ' + Style.RESET_ALL).lower()

while conv.startswith('д') or conv.startswith('l'):
    amount = input(Fore.BLUE + 'Сколько денег будем переводить? ' + Style.RESET_ALL)
    try:
        amount = float(amount)
    except:
        print(Fore.RED + 'Пожалуйста, введите число!' + Style.RESET_ALL)
        conv = input(Fore.BLUE + 'Хотите конвертировать валюту? (да или нет) ' + Style.RESET_ALL).lower()

    first = input(Fore.LIGHTYELLOW_EX + 'Из какой валюты будем переводить? ').upper()
    second = input('В какую валюту будем переводить? ' + Style.RESET_ALL).upper()

    result = convert(first, second, amount)
    print(Fore.GREEN + result)


