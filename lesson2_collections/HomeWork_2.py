def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst)==0:
        print("Wrong list")
        return
    reversed_lst = lst[::-1]
    print(reversed_lst)

print_list_reverse([1, 2, 3, 4, 5])
print_list_reverse([])
print()

def  is_valid_point(point):
    if point is None:
        return None
    if isinstance(point,tuple) and len(point)==0:
        return None
    if not isinstance(point,tuple):
        return False
    if len(point)!=2:
        return False
    x,y = point
    if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
        return False
    return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))
print()

def print_sublist_reverse(lst, start, finish):
    if lst is None or not isinstance(lst,list) or len(lst)==0:
        print("Wrong args")
        return
    if (
        not isinstance(start,int)
        or not isinstance(finish,int)
    ):
        print("Wrong args")
        return
    if start<0 or finish >=len(lst)or start>finish:
        print("Wrong args")
        return
    beginning = lst[:start]
    middle_reversed = lst[start:finish+1][::-1]
    ending = lst[finish+1:]
    print(beginning+middle_reversed+ending)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)

print()

def print_sublist_reverse_1(lst, start, finish):
    if lst is None or lst == []:
        print("Wrong args")
    elif not isinstance(lst, list):
        print("Wrong args")
    elif not isinstance(start, int) or not isinstance(finish, int):
        print("Wrong args")
    elif start < 0 or finish >= len(lst) or start > finish:
        print("Wrong args")
    else:
        lst[start:finish + 1] = lst[start:finish + 1][::-1]
        print(lst)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print_sublist_reverse([10, 20, 30, 40, 50, 60], 3, 5)
print()

def get_students_by_grade(students):
    if students is None or not isinstance(students,dict) or len(students)==0:
        return {}
    result = {}
    for name,grade in students.items():
        result.setdefault(grade,[]).append(name)

        # if grade not in result:
        #     result[grade]=[]
        # result[grade].append(name)
    return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}) )