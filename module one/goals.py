# ----------- GOAL DISPLAY ---------------

import keyword

your_name = input("Enter your username: ")
your_goal = input("Enter your goal: ")
target_month = input("Enter the month you wish to reach your goal: ")
daily_practice = 30

print("\nMY PERSONAL GOAL PLAN")

print("Username: ", your_name)
print("Goal: ", your_goal)
print("Target Month: ", target_month)
print("Daily Practice: ", daily_practice, " minutes")

print("\nstatus: ", end=" ")
print("Not started")
print("Reminder: ", end=" - ")
print("Practice everyday!")

print("\nIn one sentence: ")
print(your_name, "plans to work on", your_goal, "for", daily_practice, "minutes every day until", target_month)
print("\nWords python has reserved for itself:\n")
print(keyword.kwlist)