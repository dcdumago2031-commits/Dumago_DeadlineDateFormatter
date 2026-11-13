event_title = str(input("Enter event title: "))
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

complete_date = f"{month} {day}, {year}"

print()

print(f"Event: {event_title}")
print(f"Date: {complete_date}")
print(f"Month: {month}")
print(f"Day: {day}")