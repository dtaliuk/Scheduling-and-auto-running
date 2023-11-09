import schedule
import requests


def greeting():
    # Запишем рутинные дела в словарь
    todos_dict = {
        '08:00': 'Drink coffe',
        '11:00': 'Work meeting',
        '23:59': 'Hack the Planet!'
    }

    print("Day's tasks")

    # пробежимся циклом по словарю и выведем информацию в терминал
    for key, value in todos_dict.items():
        print(f'{key} - {value}')

    # запросим курс биткойна к доллару обратившись по API к бирже
    responce = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = responce.json()

    btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$\n"
    print(btc_price)


def main():
    # Создадим планировщик для запуска функции greeting()

    # ЗАПУСК ФУНКЦИИ ЧЕРЕЗ ОПРЕДЕЛЕННОЕ ВРЕМЯ:
    schedule.every(interval=4).seconds.do(greeting)
    schedule.every(interval=5).minutes.do(greeting)
    schedule.every().hour.do(greeting)

    schedule.every().day.at('17:49').do(greeting)
    schedule.every().thursday.do(greeting)
    schedule.every().friday.at('16:00').do(greeting)

    # создадим бесконечный цикл
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
