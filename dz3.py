# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.

import datetime

def date_after_days(days):
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date


days_to_add = 10  
result_date = date_after_days(days_to_add)
print(f"Дата через {days_to_add} дней: {result_date}")