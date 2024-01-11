from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    current_date = datetime.now()
    date_today = datetime(year=current_date.year, month=current_date.month, day=current_date.day)
    current_year = current_date.year

    # Grupuj użytkowników według dnia tygodnia, uwzględniając urodziny od dzisiaj do 7 dni w przód
    grouped_users = {}
    for user in users:
        birthday = user['birthday'].replace(year=current_year)

        # Oblicz datę 7 dni w przód od bieżącego dnia
        one_week_forward = date_today + timedelta(days=7)

        if date_today == birthday or date_today <= birthday < one_week_forward:
            day_of_week = birthday.strftime("%A")

            if day_of_week == "Saturday" or day_of_week == "Sunday":
                day_of_week = "Monday"

            if day_of_week not in grouped_users:
                grouped_users[day_of_week] = [user]
            else:
                grouped_users[day_of_week].append(user)

    # Kolejność dni tygodnia w liście
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Wyświetl listę użytkowników w odpowiednim formacie według kolejności dni tygodnia
    for day in days_of_week:
        if day in grouped_users:
            names = [user['name'] for user in grouped_users[day]]
            print(f"{day}: {', '.join(names)}")

# Przykładowa lista użytkowników
users = [
    {'name': 'Bill', 'birthday': datetime(2001, 11, 9)},
    {'name': 'Jill', 'birthday': datetime(2002, 11, 7)},
    {'name': 'Kim', 'birthday': datetime(2003, 11, 11)},
    {'name': 'Jan', 'birthday': datetime(1993, 11, 29)},
    {'name': 'Tom', 'birthday': datetime(2000, 11, 6)},
]

# Wywołanie funkcji z przykładową listą użytkowników
get_birthdays_per_week(users)
