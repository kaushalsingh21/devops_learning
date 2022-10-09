num_of_minutes = 24 * 60
units = "minutes"


def days_convertor(num_of_days):
   return f"Number of minutes in {num_of_days} days are {user_input_num * num_of_minutes} {units}"


user_input = input("Please enter the number of days:\n")

if user_input.isdigit():
    user_input_num = int(user_input)
    if user_input_num > 0:
        final_value = days_convertor(user_input_num)
        print(final_value)
    elif user_input == 0:
        print("Number of days cannot be 0")
else:
    print("The value entered is corrupt. Please enter a valid value for number of days")


