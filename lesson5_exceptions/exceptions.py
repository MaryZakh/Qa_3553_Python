# with open("user.json", "r", encoding="utf-8") as file:
#     print(file.read())

# print("START PROGRAM")
# result = 10/0
# print(result)
# print("END PROGRAM")

# def div_int(a,b):
#     return a/b
#
# print("START PROGRAM")
# res = div_int(10,0)
# print(res)
# print("END PROGRAM")


#try/except
print("START PROGRAM")
try:
    result = 10/0
    print(result)
except Exception as e:
    print("An error occurred: ",e)

print("END PROGRAM")
print()


def is_number(text):
    try:
        float(text)
        return True
    except (TypeError,ValueError):
        return False

print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Hello"))
print(is_number(None))

print()


try:
    value = int("69")
except ValueError:
    print("This is not a number")
else:
    print("The transformation was successful: ", value)
finally:
    print("This block is always executed")
