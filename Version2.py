
print("Student Event Registration")

# Get student information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")

# Get event date
year = input("Enter event year: ")
month = input("Enter event month: ")
day = input("Enter event day: ")

# Clean and format text
first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
event_name = event_name.strip().title()

full_name = first_name + " " + last_name

# Display registration summary
print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event_name)
print("Event Date:", month, day + ",", year)

print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
