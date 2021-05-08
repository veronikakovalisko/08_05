'''
Task
Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
'''
lst = [12, 4, 5]
d = {'as': 'ammm'}
def oops(ind, key):
    lst[ind]
    print(d[key])
def tr(ind, key):
    try:
        oops(ind, key)
    except IndexError:
        print("oops")
    except KeyError:
        print("oops2.0")


def check(a, b):
    a = a**2/b
    return a

if __name__ == '__main__':
    key = 'asss'
    tr(4, key)
    try:
        a = int(input("a="))
        b = int(input("b="))
        print(check(a, b))
    except ZeroDivisionError:
        print("b cann`t be 0")
    except TypeError:
        print(" a and b must be digital")


"""
Task 2
Write a function that takes in two numbers from the user via input(), 
call the numbers a and b, and then returns the value of squared a divided by b, 
construct a try-except block which raises an exception 
if the two values given by the input function were not numbers, 
and if value b was zero (cannot divide by zero).    
"""




