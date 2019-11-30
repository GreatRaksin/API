from colorama import init, Fore, Style
from currency_converter import CurrencyConverter

init()

conv = input(Fore.BLUE + 'Хотите конвертировать валюту? (да или нет) ' + Style.RESET_ALL).lower()

while conv.startswith(('д', 'l', 'd')):
    amount = input(Fore.BLUE + 'Сколько денег будем переводить? ' + Style.RESET_ALL)
    try:
        amount = float(amount)
    except:
        print(Fore.RED + 'Пожалуйста, введите число!' + Style.RESET_ALL)
        conv = input(Fore.BLUE + 'Хотите конвертировать валюту? (да или нет) ' + Style.RESET_ALL).lower()

    first = input(Fore.LIGHTYELLOW_EX + 'Из какой валюты будем переводить? ').upper()
    second = input('В какую валюту будем переводить? ' + Style.RESET_ALL).upper()

    c = CurrencyConverter()

    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '%.2f' % c.convert(amount, first, second) + Style.RESET_ALL)
    conv = input(Fore.BLUE + 'Хотите еще раз конвертировать валюту? (да или нет) ' + Style.RESET_ALL).lower()

print(Style.BRIGHT + Fore.LIGHTCYAN_EX + 'Хорошего дня!')
