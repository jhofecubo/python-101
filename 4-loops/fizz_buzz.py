# Fizz Buzz 🐝
# Codédex

for number in range(0,101):
    if number%5!=0 and number%3!=0:
        print(number)
    elif number%5==0 and number%3==0:
        print("fizzbuzz")
    elif number%3==0:
        print("fizz")
    elif number%5==0:
        print("buzz")
