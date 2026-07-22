import csv
import json
from pathlib import Path


def save_shopping_list(items):
    with open("shopping.txt", "w", encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")


items = [
    "Milk",
    "Bread",
    "Apples",
    "Coffee"
]

save_shopping_list(items)

with open("shopping.txt", "r", encoding="utf-8") as file:
    print(file.read())
    print()


def read_students(filename):
    with open("students.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student:{row['name']}({row['age']})")
            # print(row)


read_students("students.csv")

print()


def save_profile(name, age, city):
    profile = {
        "name": name,
        "age": age,
        "city": city
    }

    with open("profile.json", "w", encoding="utf-8") as file:
        json.dump(profile, file, indent=4)


save_profile("Mariia", "30", "Haifa")

print()


def create_reports_folder():
    reports_dir = Path("reports_1")
    reports_dir.mkdir(exist_ok=True)
    result_file = reports_dir / "result.txt"
    with open(result_file, "w", encoding="utf-8") as file:
        file.write("Homework completed successfully!")


create_reports_folder()
