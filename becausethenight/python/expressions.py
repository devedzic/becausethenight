# Demonstrates how operators and expressions work in Python

def demonstrate_arithmetic_operators():
    a = ((7//3)**3) % 3 + 2                 # the result should be 4
    print('Result:', a)

def demonstrate_relational_operators():
    if 1 >= 3:
        print('1 >= 3')
    else:
        print('1 < 3')
    print()

    from datetime import date
    d1 = date(2018, 1, 2)
    print('d1 =', d1)
    d2 = date.today()
    print('d2 =', d2)
    if d1 > d2:
        print("Future")
    else:
        print("Past")
    print()

    d3 = date.today()
    print('d3 =', d3)
    if d2 is d3:                    # returns False (since d2 and d3 do not point to the same object)
        print('d2 is d3')
    else:
        print('d2 is not d3')
    if d2 == d3:                    # returns True (since d2 and d3 are equal)
        print('d2 == d3')
    else:
        print('d2 != d3')
    print()

    a = None
    print('a =', a)
    print('Type of None:', type(None))

def demonstrate_logical_operators():
    print('True and False:', True and False)
    print('True or False:', True or False)
    print('not True:', not True)
    print('None and 1:', None and 1)
    print()

    from datetime import date
    d1 = date(2018, 1, 2)
    print('d1 =', d1)
    d2 = date.today()
    print('d2 =', d2)
    print()

    print('d2 and None:', d2 and None)
    print('d2 > None:', d2 > None)      # generates an error:
                                        # TypeError: '>' not supported between instances of 'datetime.date' and 'NoneType'

