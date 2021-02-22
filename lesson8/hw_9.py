from datetime import datetime, date
import calendar

def congratulate(users):
    lis = []
    present_data = datetime(year=2021, month=2, day=25) #datetime.now()
    week_day = present_data.weekday()
    num = calendar.monthrange(present_data.year, present_data.month)
    num_1 = num[1]
    if week_day == 0:
        n = -2
    else:
        n = 6- week_day-1

    for i in range(7):
        if present_data.day + i + n <= num_1:
            lis.append(datetime(year = present_data.year, month = present_data.month,
        day = (present_data.day+i+n)))
        else:
            
           lis.append(datetime(year = present_data.year, month = present_data.month + 1,
        day = (present_data.day+i+n-num_1))) 

   
    mond = ''
    tue = ''
    wen = ''
    thu = ''
    fri = ''
    for data in lis:
        days = data.day
        mon = data.month
        for person in users:
            days_person = person['birthday'].day
            month_person = person['birthday'].month
            if mon == month_person and days == days_person:
                if data.weekday() == 5 or data.weekday() == 6 or data.weekday() == 0:
                    mond += (person['Name']+', ')
                elif data.weekday() == 1:
                    tue += (person['Name']+', ')
                elif data.weekday() == 2:
                    wen += (person['Name']+', ')
                elif data.weekday() == 3:
                    thu += (person['Name']+', ')
                elif data.weekday() == 4:
                    fri += (person['Name']+', ')

    if mond:
        print('Monday: '+mond[:-2])
    if tue:
        print('Tuesday: '+tue[:-2])
    if wen:
        print('Wenesday: '+wen[:-2])
    if thu:
        print('Thursday: '+thu[:-2])
    if fri:
        print('Friday: '+fri[:-2])
            







user = [{'Name': 'Ivan', 'birthday': datetime(year=1980, month=3, day=1)},
{'Name': 'Bill', 'birthday': datetime(year=1988, month=3, day=2)},
{'Name': 'Semen', 'birthday': datetime(year=1980, month=3, day=8)},
{'Name': 'Kost', 'birthday': datetime(year=1980, month=3, day=6)},
{'Name': 'Alex', 'birthday': datetime(year=1980, month=3, day=4)},
{'Name': 'Viola', 'birthday': datetime(year=1980, month=3, day=5)}
]

congratulate(user)