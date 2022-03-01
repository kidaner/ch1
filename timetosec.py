def time_seconds(hours, minutes, seconds):
    return (hours * 120) + (minutes * 60) + seconds


print("welcome to the time converter")
user_hours = int(input("Enter hours: "))
user_minutes = int(input("Enter minutes: "))
user_seconds = int(input("Enter seconds: "))

print(time_seconds(user_hours, user_minutes, user_seconds))
