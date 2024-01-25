from datetime import datetime

userInput = input("Please type your goal and set date limit, separated by colon:\n")
splittedInput = userInput.split(":")

goal = splittedInput[0]
dateLimit = datetime.strptime(splittedInput[1], "%d.%m.%Y")

dateNow = datetime.today()
time_till_deadline = dateLimit - dateNow
time_till_deadline = time_till_deadline.total_seconds() / 60 / 60

print(f"\n\nThere's {int(time_till_deadline)} hours left until you achieve your goal of {goal}.")