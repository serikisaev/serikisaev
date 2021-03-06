import time
import random


questions_list = [
    ('2 + 2 = 4', 'T'),
    ('3 + 2 = 7', 'F'),
    ('5 + 2 = 7', 'T'),
    ('2 + 1 = 3', 'T'),
    ('5 + 4 = 10', 'F'),
    ('4 + 3 = 8', 'F'),
    ('5 * 5 = 26', 'F'),
    ('5 * 3 = 15', 'T')
]

random.shuffle(questions_list)


def line():
    count = len(questions_list)
    score = 0
    start_time = time.perf_counter()
    while count != 0:
        x = questions_list.pop(0)

        answer = input('Правильно ли утверждение что ' + x[0] + '\nОтвет в формате F или T: ')
        if answer == x[1]:
            print('Ты прав чувак!')
            score += 1
        else:
            print('Не бро, учись считать...')
        count -= 1
    end_time = time.perf_counter()
    ready_time = end_time - start_time

    print('\n\n\nОчкодранов набрал: ' + str(score))
    print('Выполнил тест за: ' + str(ready_time) + ' секындыф')


if __name__ == '__main__':
    line()
