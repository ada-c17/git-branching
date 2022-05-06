
from datetime import datetime

#creating a simple function
""" Git Branching """


def good_morning():
  weekday = datetime.today().strftime("%A")
  print(f"Good morning! Happy {weekday}~")

good_morning()
print("wooo")