age = input("What is your current age?")

days = (365*60)-(365*int(age))
weeks = (52*60)-(52*int(age))
months = (12*60)-(12*int(age))

print(f"you have {days} days, {weeks} weeks, and {months} months left")

