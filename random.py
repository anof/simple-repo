import random
import datetime

def generate_random_birthday(start_year=1970, end_year=2005):
    """
    Generates a random birthday between the given start and end years.

    Args:
        start_year (int): The earliest possible year for the birthday.
        end_year (int): The latest possible year for the birthday.

    Returns:
        datetime.date: A date object representing the random birthday.
    """
    # Create start and end date objects from the given years
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)

    # Calculate the total number of days between the start and end dates
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    # Generate a random number of days to add to the start date
    random_number_of_days = random.randrange(days_between_dates)

    # Calculate the random date
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date

def create_birthday_list(num_people=25):
    """
    Generates a list of lists, with each inner list containing a
    person's name and a random birthday.

    Args:
        num_people (int): The number of people to generate birthdays for.

    Returns:
        list: A list of lists, e.g., [['Person 1', 'YYYY-MM-DD'], ...]
    """
    birthday_list = []
    for i in range(1, num_people + 1):
        person_name = f"Person {i}"
        birthday = generate_random_birthday()
        # Format the date as a string for readability
        formatted_birthday = birthday.strftime("%Y-%m-%d")
        birthday_list.append([person_name, formatted_birthday])
    return birthday_list

# --- Main Execution ---
if __name__ == "__main__":
    # Generate a list for 23 people, as in the classic birthday problem
    number_of_entries = 23
    people_with_birthdays = create_birthday_list(number_of_entries)

    # Print the generated list
    print(f"Generated list of {number_of_entries} people with random birthdays:")
    for person in people_with_birthdays:
        print(f"- {person[0]}: {person[1]}")

