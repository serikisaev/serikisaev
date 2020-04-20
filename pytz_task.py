import pytz
import datetime


def return_timezones_list():
    quantity_timezones = int(input('Сколько нужно временных зон вывести?: '))
    count = 0
    time_zones_list = []
    for country in pytz.country_names:

        if count == quantity_timezones:
            break
        else:
            time_zones_list.append((country, (pytz.country_names[country], pytz.country_timezones.get(country))))
        count += 1
    for i in time_zones_list:
        print(i[0], i[1])
    return time_zones_list


t = return_timezones_list()


def main():
    while True:
        code_country = input('\nДля выхода введите "q"\nВведите двухбуквенный код страны: ')
        if code_country == 'q':
            break
        else:
            for i in t:
                if code_country == i[0]:
                    time_zone = pytz.timezone(i[1][1][0])
                    print(f'\nСейчас время в {i[1][0]}: {datetime.datetime.now(tz=time_zone)}')
                    print(f'Сейчас время в UTC:{datetime.datetime.utcnow()}')


if __name__ == '__main__':
    main()
