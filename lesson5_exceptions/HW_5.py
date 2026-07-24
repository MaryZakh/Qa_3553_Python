def get_list_element(items, index):
    try:
        return items[index]
    except IndexError:
        return "Index is out of range"

numbers = [10, 20, 30]
print(get_list_element(numbers, 1))
print(get_list_element(numbers, 10))

print()

def get_user_data(user, key):
    try:
        return user[key]
    except KeyError:
        return "Key was not found "

user = {
    "name": "Anna",
    "age": 30
}

print(get_user_data(user, "name"))
print(get_user_data(user, "email"))
print()

def calculate_average(first_value, second_value):
    try:
        first_num = float(first_value)
        second_num = float(second_value)
    except ValueError:
        return "Value must be a number"
    except TypeError:
       return "Invalid data type"

    return (first_num+second_num)/2

print(calculate_average("10", "20"))
print(calculate_average("hello", "20"))
print(calculate_average(None, 20))
print()

# def read_number():
#     try:
#         user_input = input("Enter a number: ")
#         number = int(user_input)
#     except ValueError:
#         print("Invalid number")
#
#     else:
#         print("Number was entered successfully")
#     finally:
#         print("Program finished")
#
# read_number()
print()

def validate_age(age):
    if age<0:
        raise ValueError("Age cannot be negative")
    if age>120:
        raise ValueError("Age is not realistic")

# validate_age(25)
# validate_age(-5)
# validate_age(165)

try:
    validate_age(25)
except ValueError as error:
    print(error)

try:
    print(validate_age(-5))
except ValueError as error:
    print(error)

try:
    print(validate_age(165))
except ValueError as error:
    print(error)

print("******************")

ages = [17,25,-5,150,40,300,46,99,119]
for age in ages:
    try:
        print(validate_age(age))
    except ValueError as error:
        print(error)