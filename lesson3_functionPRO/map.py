numbers = [1, 2, 3, 4, 5]

squared = map(lambda x: x ** 2, numbers)
print(squared)
print(list(squared))
print()

def to_upper(s):
    return s.upper()

statuses = ["passed","failed","skipped"]
upper_statuses = list(map(to_upper,statuses))
print(upper_statuses)