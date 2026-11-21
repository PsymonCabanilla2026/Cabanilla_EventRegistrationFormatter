
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

# Display registration summary
print("\nStudent Event Registration Summary")
print("Name:", first_name, last_name)
print("Section:", section)
print("Event:", event_name)
print("Event Date:", month, day + ",", year)
