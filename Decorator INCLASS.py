def my_decorator(original_function):
    print(f"The decorator was called on {original_function.__name__}")
    def modified_function():
        print(f"Do some stuff before {original_function.__name__}")
        original_function()
        print(f"Do some stuff after {original_function.__name__}")
    return modified_function

# @my_decorator
def another_function():
    print("Do main function stuff")

# roughly equivalent to @my_decorator before the function definition
# another_function = my_decorator(another_function)

@my_decorator
def yet_another_function():
    print("Do yet more stuff")