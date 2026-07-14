def double(x):
    return x*2

double_lambda = lambda x: x*2

# double_lambda_1 = lambda x: x*2 if x>0 else -x

print(double(5))
print(double_lambda(5))
# print(double_lambda_1(-3))

print()

add = lambda a,b: a+b
print(add(3,4))

is_even = lambda n: n%2 ==0
print(is_even(10))
print(is_even(7))

