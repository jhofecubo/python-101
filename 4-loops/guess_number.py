
tries=0
guess = 0

while guess != 6 and tries<= 4:
  guess = int(input("Guess the number:  "))
  tries= tries +1

if guess == 6:
    print("You got it!")
else:
    print("No more attemps allowed")
