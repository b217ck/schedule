from datetime import date, timedelta

days = ["Понедельник", "Вторник", "Среда",
        "Четверг", "Пятница", "Суббота", "Воскресенье"]

print('Введите год в формате ГГГГ:')
dt_year = int(input())
print('Введите месяц в формате ММ:')
dt_month = int(input())
print('Введите день в формате ДД:')
dt_day = int(input())

date_obj = date(dt_year, dt_month, dt_day)
print('Дата начала:', date_obj)

future_date = date_obj + timedelta(days=30)
print('Дата окончания (+30 дней):',future_date)
print('Расписание занятий:')

count_date = date_obj
i = 0
for i in range(30):
    while future_date > count_date:
        if count_date.weekday() != 5:
            count_date = count_date + timedelta(days=1)
            i = i + 1
            print(i, '- учебный день:')
            if i % 2 ==0:
                print(count_date, days[count_date.weekday()], "- сдача задания или урока")
            else:
                print(count_date, days[count_date.weekday()], "- решение задания или урока")
        else:
            count_date = count_date + timedelta(days=1)
            print(count_date, days[count_date.weekday()], "- отдых")