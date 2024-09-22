# Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.

import datetime

now = datetime.datetime.now()

formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')

day_of_week = now.strftime('%A')
week_number = now.isocalendar()[1]

print(f"Текущая дата и время: {formatted_time}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")