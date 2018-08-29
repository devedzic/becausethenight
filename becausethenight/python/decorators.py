'''Demonstrates pass, returning None, functions as parameters of other functions,
functions as return values of other functions, user-defined and built-in decorators and lambdas'''


from becausethenight.python import functions


def return_None():
    '''Demonstrates returning None and the pass statement.'''

    # print(None)
    pass

def pass_function_as_parameter(f, *args):
    '''Demonstrates using another function as a parameter. It works because functions are objects.'''

    f(*args)

# def return_function(full_name):
#     name = full_name.split()
#     return name

def return_function(full_name, first_name_flag):

    name = full_name.split()

    def return_first_name():
        return name[0]

    def return_family_name():
        return name[1]

    if first_name_flag:
        return return_first_name
    else:
        return return_family_name

def return_function_with_args(*args):

    def return_empty():
        return []

    def return_tuple(*args):                            # '*' is important here; without it, args is a positional arg!
        return tuple(args)

    if len(list(args)) == 0:
        return return_empty
    else:
        return return_tuple

def show_author(f):
    def wrapper():
        pass

if __name__ == '__main__':

    return_None()                                       # returning None
    print(return_None())
    print()

    pass_function_as_parameter(return_None)             # function as a parameter: just the function's name, not ()!
    pass_function_as_parameter(
        functions.use_flexible_arg_list,                # function as a parameter: just the function's name, not ()!
        "Just a prompt")
    pass_function_as_parameter(
        functions.demonstrate_annotations,              # function as a parameter: just the function's name, not ()!
        'Patti Smith',
        'Because the Night')
    print()

    f = return_function('Patti Smith', True)
    print('f:', f)
    print('type(f):', type(f))
    print('f():', f())
    print()

    f = return_function_with_args('Patti Smith', True)
    print('f:', f)
    print('type(f):', type(f))
    f()
    print('f():', f())
    print()
