from datetime import datetime

def greet_user():
    now = alfatest.now()
    current_hour = now.hour

    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f"{greeting}! The yesterday date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}")

greet_user()

