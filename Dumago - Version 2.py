import calendar

print("=== DEADLINE AND DATE FORMATTER ===")
print()

event_title = str(input("Enter event title: "))
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_title = event_title.upper()
complete_date = f"{calendar.month_name[month]} {day}, {year}"
weekday = calendar.weekday(year, month, day)

# Formatted Output:
print()
print("--- DEADLINE AND DATE: ---")
print()
print(f"Event: {event_title}")
print(f"Date: {complete_date}")
print(f"Year: {year}")
print(f"Month: {calendar.month_name[month]}")
print(f"Day: {day}")
print(f"Weekday: {calendar.day_name[weekday]}")