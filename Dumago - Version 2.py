import calendar

print("=== DEADLINE AND DATE FORMATTER ===")
print()

event_title = str(input("Enter event title: "))
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

complete_date = f"{calendar.month_name[month]} {day}, {year}"

# Formatted Output:
print()
print("--- DEADLINE AND DATE: ---")
print()
print(f"Event: {event_title}")
print(f"Date: {complete_date}")
print(f"Month: {calendar.month_name[month]}")
print(f"Day: {day}")