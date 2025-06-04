# if statement
import sys

age =int(sys.argv[1])
if age>=18:
    print("you can vote")



# else statement
else:
    print("you cannot vote")


# elif statement
import sys

marks=int(sys.argv[1])

if marks>=90:
    print("your grade is GRADE A")
elif marks>=70:
    print("your grade is GRADE B")
elif marks>=50:
    print("your grade is GRADE C")
else:
    print("you have failed")


# nested if
import sys
age =int(sys.argv[1])
has_license=sys.argv[2]

if age>=18:
    if has_license == "yes":
        print("you can drive")
    else:
        print("go and take license  ")

else:
    print("you are too young to drive")