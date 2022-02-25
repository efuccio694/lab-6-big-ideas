name = input("What is your name?: ")
age = int(input("How old are you currently?: "))
current_year = int(input("What is the current year?: "))
passed = True;
is_passed = input("Has your birthday passed this year already? Type yes or no: ")

if is_passed == 'yes':
    passed = True
    offset = 0
else:
    passed = False
    offset = -1

birthyear = current_year-age+offset

print(f"Hello {name}! In the year {current_year}, you were born {age} years ago in {birthyear}.")