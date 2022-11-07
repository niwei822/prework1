firstName = input("What’s your first name?: ")
lastName = input("What’s your last name?: ")
color = input("What’s your favorite color?: ")
pets = input("How many pets do you have?: ")

message = (
    f"Tell us your first name: {firstName}. "\
    f"Tell us your last name: {lastName}. "\
    f"Tell us your favorite color: {color}. "\
    f"Tell us how many pets you have: {pets}. "\
    f"Great! So your name is {firstName} {lastName}, your favorite color is {color} and you have {pets} pets. Nice to meet you! " )
print(message)