def create_profile(name, age=18, city='Unknown'):
    return {
        "name": name,
        "age": age,
        "city": city
    }


print(create_profile("Anna"))
print(create_profile("Tom", 25))
print(create_profile(city="Haifa", name="Igor"))
print()


def sum_even_numbers(*numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number
    return total


print(sum_even_numbers(1, 2, 3, 4, 5, 6))  # 12
print(sum_even_numbers(7, 9))  # 0
print(sum_even_numbers())  # 0

print()


def sum_even_numbers_1(*numbers):
    return sum(filter(lambda x: x % 2 == 0, numbers))


print(sum_even_numbers(1, 2, 3, 4, 5, 6))  # 12
print(sum_even_numbers(7, 9))  # 0
print(sum_even_numbers())  # 0
print()


def print_pet_info(name, **info):
    print(f"Name:{name}")
    if not info:
        print("No additional information")
        return
    for key, value in info.items():
        print(f"{key}:{value}")


print_pet_info(
    "Lucky",
    age=4,
    color="White",
    breed="Spitz"
)
print()
print_pet_info("Lucky")
print()

def merge_lists(*lists):
    result = []

    for current_list in lists:
        for item in current_list:
            result.append(item)
    return result

print(merge_lists(
    [1, 25],
    [3,8,3],
    [4, 5,456],
    []
))

print()

def build_message(*words, separator=" "):
    return separator.join(words)

print(build_message("Hello", "world"))
print(build_message("2026", "07", "15", separator="-"))
print(build_message())
