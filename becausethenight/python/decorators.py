"""Demonstrates pass, returning None, functions as parameters of other functions,
functions as return values of other functions, user-defined and built-in decorators and lambdas
"""


import functools


def return_None():
    """Demonstrates returning None and the pass statement.
    """

    # print(None)
    pass


def pass_function_as_parameter(f, *args):
    """Demonstrates using another function as a parameter. It works because functions are objects.
    """

    f(*args)

# def return_function(full_name):
#     name = full_name.split()
#     return name


def return_function(full_name, first_name_flag):
    """Demonstrates using a function as the return value from another function.
    """

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
    """Demonstrates using a function as the return value from another function.
    The returned function has parameters/arguments.
    """

    def return_empty():
        return []

    def return_tuple(*parameters):                      # '*' is important here; without it, args is a positional arg!
        return tuple(parameters)

    if len(args) == 0:
        return return_empty
    else:
        return return_tuple


def show_author(artwork_f):
    """Demonstrates how to develop a decorator. Uses the decorator-writing pattern:
    import functools
    def decorator(func):
        @functools.wraps(func)			                # preserves func's identity after it's decorated
        def wrapper_decorator(*args, **kwargs):
            # Do something before
            value = func(*args, **kwargs)
            # Do something after
            return value
        return wrapper_decorator
    """

    @functools.wraps(artwork_f)
    def wrapper(*args):
        # Do something before
        authors = list(args)
        del authors[0]                                  # assuming the first arg is the song title
        i = 0
        for a in authors:                               # looks more compact wth an iterator
            print(a, end='')
            if i < (len(authors) - 1):
                print(", ", end='')
                i += 1
            else:
                print(': ', end='')
        # Alternatively:
        # for i, a in enumerate(authors):
        #     print(a, end='')
        #     if i < (len(authors) - 1):
        #         print(", ", end='')
        #     else:
        #         print(': ', end='')

        # Decorate artwork_f
        decorated_artwork_f = artwork_f(*args)
        # Do something after
        print('--------------------------')
        return decorated_artwork_f
    return wrapper


@show_author                                            # decorator; omit it if decorating manually (see at the end)
def print_song(title, *authors):
    print(title)


if __name__ == '__main__':

    from becausethenight.python import functions

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
    f('Patti Smith', 'Bruce Springsteen', True)
    print('f():', f('Patti Smith', 'Bruce Springsteen', True))
    print()

    # print_song("Because the Night", "Patti Smith")
    # print_song = show_author(print_song)              # decorate manually
    print_song("Because the Night",
               "Patti Smith",
               "Bruce Springsteen")
    print()
