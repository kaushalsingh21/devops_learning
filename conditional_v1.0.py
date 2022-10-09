num_of_minutes = 24 * 60
units = "minutes"


def days_convertor(num_of_days):
    if num_of_days > 0:
        return f"Number of minutes in {num_of_days} days are {user_input_num * num_of_minutes} {units}"
    elif num_of_days == 0:
        return "Number of days cannot be 0"
    else:
        return "Please enter a valid number. Number of days cannot be negative"


user_input = input("Please enter the number of days:\n")

if user_input.isdigit():
    user_input_num=int(user_input)
    final_value = days_convertor(user_input_num)
    print(final_value)
else:
    print("The value entered is corrupt. Please enter a valid value for number of days")


