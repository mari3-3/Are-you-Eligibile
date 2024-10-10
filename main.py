print("Let's play a game'0'")
print("It's called ARE YOU ELIGIBLE!!")
print("This is a game where you find out if you can vote or not")
print("I hope you're ready to play because it's not a choice O-0")
print()

age = int(input ("Please enter your age: "))
if age >= 18:
  age == True
else:
  print()
  print("NO MINORS ALLOWED^0^!")
  exit()
citizen = input("Are you a citizen, (y/n): ")
if citizen == "y":
  citizen == True
else:
  print()
  print("You might want to fix that buddy <_<'")
  exit()
registered = input("I hope you're registered to vote? (y/n): ")
if registered =="y":
  registered == True
else:
  print()
  print("Then what are you waiting for?!")
  exit()
jail = input("Are you incarcerated (did you do jail time?) (y/n): ")
if jail == "n":
  jail == True
else: 
  print()
  print("Get out of here \./")
  exit()
if age >=18 and citizen == "y" and registered == "y" and jail == "n":
  print()
  print("YOU CAN VOTE ^.^!")
  print("Thanks for playing @_@")
