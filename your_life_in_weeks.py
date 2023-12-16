
age = input("What is your current age?")

age_as_int = int(age)

years_remaning = 90 - age_as_int

days_remainng = years_remaning * 365

weeks_remaning = years_remaning * 52

months_remainng = years_remaning * 12

print(f"you have {years_remaning} years, {days_remainng} days, {weeks_remaning} weeks and  {months_remainng} months remaning")