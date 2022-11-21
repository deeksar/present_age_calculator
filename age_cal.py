#current age calculator
age = input("What is your current age?")
age_left=int(age)
d=90*365-age_left*365
w=90*52-age_left*52
m=90*12-age_left*12
if(age_left<=90):
  print(f"You have {d} days, {w} weeks, and {m} months left.")
