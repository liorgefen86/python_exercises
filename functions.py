# functions exist in all programming languages and are used to isolate
# a part of a code that can then be used several times without having
# to write the entire again and again.
# a function is defined using 'def' keyword


# below is a simple function definition. The function has a single
# parameter, which needs to be a str, and has a default value 'lior'.
# It is not possible to overload methods or functions in python


def greeting(name: str = 'lior'):
    """
    Take a single argument in and print a greeting sentence.
    :param name:
    :return: None
    """
    print(f'Hello, {name}')


greeting('daria')
greeting()
greeting(name='eyal')  # when calling a function using the parameters
# names, it is called keyword argument. It is useful when there is
# multiple parameters but we don't remember the order. It also gives
# more clarity the function call: the parameter value is known just
# by looking at the function call.


# below function is taking an arbitrary number of arguments using
# the argument *args. I added input and output data types but they
# are mostly used as an indication. Python won't throw an error because
# a string is used instead of a float.
# args is the usual way to call this argument but it could be called
# in any other way, as long as the variable is preceded by *


def add(*args: float) -> float:
    # below is a docstring used to document a function.
    # a docstring should be added to each function explaining what the
    # function is doing and how. docstrings should be used with
    # comments. Adding a docstring to a function is good, but adding
    # both, docstring and comments is better.
    """
    add(*float) -> float\n
    function take a list of arguments and add them.
    """

    s = args[0]
    for i in args[1:]:
        s += i
    return s


# below function is using *args (seen above) and **kwargs. The latest
# is used to input an arbitrary number of names arguments, in the form,
# from function call: var=value. *args and **kwargs need to be after
# the arguments with or without default values. **kwargs is coming
# after *args.


def greetings(first_name: str, last_name: str, *args, **kwargs):
    sentence = f'Hello, {first_name.capitalize()} {last_name.capitalize()}\n'
    for key, value in kwargs.items():
        sentence += f'{key}: {value}\n'
    for word in args:
        sentence += f'{word}\n'
    print(sentence)


print(add(4))
print(add(4, 5, 6, 7, 8, 9))
print(add('d', 'a', 'r', 'i', 'a'))
greetings('lior', 'gefen', 'pc', 'cats', 'nature', weight=83, height=173)
