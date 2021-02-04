
month = input("Enter the name of a month: ")

days = 31

if month == "april" or month == "june" or  month == "september" or month == "november": days = 30
elif month == "february": days = 28 or 29

print(month, "has", days, "days in it.")

