def print_config(**kwargs):
    print(type(kwargs), kwargs)
    return

print(print_config(browser="chrome", headless=True,timeout=30))
print(print_config())

def create_user(**data):
    return data

user = create_user(name = "Anna", role = "admin")
print(user)
# user = create_user("name":"Anna")

def example (a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

example(1,2,3,4,name ="Anna")
example(1,None,3,4,name ="Anna")