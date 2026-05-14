from datetime import datetime, date

dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert string to date
dob = datetime.strptime(dob_input, "%Y-%m-%d").date()

def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year

    # Check if birthday has occurred this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age


print("Your age is:", calculate_age(dob))