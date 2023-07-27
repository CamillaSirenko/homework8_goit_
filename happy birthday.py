from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().date()
    # Знаходимо перший день поточного тижня (понеділок)
    start_of_week = today - timedelta(days=today.weekday())
    # Знаходимо останній день наступного тижня (неділя)
    end_of_week = start_of_week + timedelta(days=13)
    
    birthdays_this_week = []
    weekends_birthdays = []
    
    for user in users:
        birthday = user.get('birthday')
        if birthday:
            birthday_date = birthday.date()
            if start_of_week <= birthday_date <= end_of_week:
                if birthday_date.weekday() in [5, 6]:  # Якщо день народження вихідний, то переносимо на понеділок
                    weekends_birthdays.append(user)
                else:
                    birthdays_this_week.append(user)
    
    if birthdays_this_week:
        print("Користувачі, яких потрібно привітати з днем народження на наступному тижні:")
        for user in birthdays_this_week:
            print(f"{user['name']} - {user['birthday'].strftime('%Y-%m-%d')}")
    
    if weekends_birthdays:
        print("\nКористувачі, у яких день народження був на вихідних і потрібно привітати в понеділок:")
        for user in weekends_birthdays:
            print(f"{user['name']} - {user['birthday'].strftime('%Y-%m-%d')}")
    
    if not birthdays_this_week and not weekends_birthdays:
        print("На наступному тижні немає днів народження.")

# Приклад використання:
users = [
    {'name': 'Ричард', 'birthday': datetime(1990, 7, 28)},
    {'name': 'Марія', 'birthday': datetime(1985, 7, 25)},
    {'name': 'Петро', 'birthday': datetime(1995, 7, 30)},
    {'name': 'Олексій', 'birthday': datetime(1992, 7, 24)},
    {'name': 'Оксана', 'birthday': datetime(2000, 7, 27)},
    {'name': 'Анна', 'birthday': datetime(1988, 8, 2)},
    {'name': 'Ольга', 'birthday': datetime(1991, 7, 31)},
    {'name': 'Олена', 'birthday': datetime(1987, 8, 1)},
]

get_birthdays_per_week(users)