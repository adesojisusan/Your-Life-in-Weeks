
age = input("What is your current age?")
new_age = int(age)

number_of_years_remaining = 90 - new_age
number_of_weeks_remaining = number_of_years_remaining * 52
number_of_days_remaining = number_of_years_remaining * 365

print(f"you have {number_of_years_remaining} years, {number_of_weeks_remaining} weeks, {number_of_days_remaining}days left.")
