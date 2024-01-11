
# Birthday Reminder

## Zadanie

Implementacja funkcji w języku Python, umożliwiającej wyświetlenie listy współpracowników, którym należy złożyć życzenia z okazji ich urodzin w tym tygodniu.

### Opis funkcji

```python
def get_birthdays_per_week(users):
    """
    Wyświetla listę użytkowników, którym należy złożyć życzenia z okazji urodzin w bieżącym tygodniu.
    
    :param users: Lista słowników zawierających imiona (klucz: 'name') i daty urodzin (klucz: 'birthday').
    :type users: list
    """
    # Implementacja funkcji...
```

### Przykład użycia

```python
# Przykładowa lista użytkowników
users = [
    {'name': 'Bill', 'birthday': datetime.datetime(1990, 1, 5)},
    {'name': 'Jill', 'birthday': datetime.datetime(1985, 12, 28)},
    {'name': 'Kim', 'birthday': datetime.datetime(1995, 1, 10)},
    {'name': 'Jan', 'birthday': datetime.datetime(1988, 12, 31)}
]

# Wywołanie funkcji
get_birthdays_per_week(users)
```

### Oczekiwane wyjście

```
Monday: Jill
Friday: Bill, Kim, Jan
```

### Warunki akceptacji

- Funkcja `get_birthdays_per_week` wyświetla osoby obchodzące urodziny w formacie: `Monday: Bill, Jill`
- Użytkownicy, których urodziny wypadły w weekend, dostają życzenia w poniedziałek.
- Funkcja wyświetla użytkowników obchodzących urodziny tydzień przed bieżącym dniem.
- Tydzień zaczyna się w poniedziałek.

### Testowanie

W celach debugowania, utwórz testową listę `users` i wypełnij ją samodzielnie, następnie użyj funkcji `get_birthdays_per_week` do wyświetlenia rezultatów.


# Birthday Reminder

## Task

Implement a Python function that allows displaying a list of coworkers who need to be wished a happy birthday this week.

### Function Description

```python
def get_birthdays_per_week(users):
    """
    Displays a list of users who should be wished a happy birthday this week.
    
    :param users: A list of dictionaries containing names (key: 'name') and birthdates (key: 'birthday').
    :type users: list
    """
    # Implementation of the function...
```

### Example Usage

```python
# Sample list of users
users = [
    {'name': 'Bill', 'birthday': datetime.datetime(1990, 1, 5)},
    {'name': 'Jill', 'birthday': datetime.datetime(1985, 12, 28)},
    {'name': 'Kim', 'birthday': datetime.datetime(1995, 1, 10)},
    {'name': 'Jan', 'birthday': datetime.datetime(1988, 12, 31)}
]

# Function call
get_birthdays_per_week(users)
```

### Expected Output

```
Monday: Jill
Friday: Bill, Kim, Jan
```

### Acceptance Criteria

- The `get_birthdays_per_week` function displays individuals celebrating birthdays in the format: `Monday: Bill, Jill`.
- Users whose birthdays fall on the weekend should receive wishes on Monday.
- The function displays users celebrating birthdays one week before the current date.
- The week starts on Monday.

### Testing

For debugging purposes, create a test list of `users` and fill it manually, then use the `get_birthdays_per_week` function to display the results.


