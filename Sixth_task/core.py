import csv
from datetime import datetime


def rus_to_eng(text):
    choices = {'Январь': 'January', 'Февраль': 'February', 'Март': 'March', 'Апрель': 'April', 'Май': 'May', 'Июнь': 'June', 'Июль': 'July', 'Август': 'August', 'Сентябрь': 'September', 'Октябрь': 'October', 'Ноябрь': 'November', 'Декабрь': 'December'}
    for rus, eng in choices.items():
        text = text.replace(rus, eng)
    return text


date = input('Введите дату в формате dd.mm.yyyy hh:mm: ')
date = datetime.strptime(date, '%d.%m.%Y %H:%M')
with open('13.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    people_list = []
    for line in reader:
        if line[0] in ['Фамилия', 'Среднее по группе', 'Общее среднее']:
            continue
        if float(line[9].replace(',', '.')) < 6.0:
            continue
        finish = datetime.strptime(rus_to_eng(line[7]), u'%d %B %Y  %H:%M')
        if finish <= date:
            continue
        people_list.append('{} {}'.format(line[0], line[1]))
print('Всего сдало:', len(people_list))
for person in people_list:
    print(person)
