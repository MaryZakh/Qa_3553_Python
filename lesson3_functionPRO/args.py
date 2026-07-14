def total (*args):
    print(type(args), args)
    return sum(args)

print(total(1,2,3))
print(total(10,20))
print(total(10,20,40,80,90))
print(total())
print()

def print_scores(student, *scores):
    print(f"Student: {student}")
    print("Scores: ", scores)

print_scores("Anna", 90,85,100)
print_scores("Bob", 75)

print()

def check_status_codes(*codes):
    for code in codes:
        assert code ==200

print(check_status_codes(200,200,200))
print(check_status_codes(200,404,200))

