
def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the function
    error message: "A list was not passed into the function"
    if number is empty return False
    if the number of even numbers is odd, return False
    if the number of even numbers is 0, return False
    if the number of even numbers is even, return True
    """
    if isinstance(numbers, list):
        if numbers == []:
            return False
        else:
            evens = 0
        for n in numbers:
            if n % 2 == 0:
                evens += 1
            # else:
            #     return False
        if evens:
            return evens % 2 == 0
        else:
            return False
    else:
        raise TypeError("A list was not passed into the function")


# this allows us to limit this function to be run only when is called
# in this file, with command python3 evens.py
# it won't be called if the function is called in other file


if __name__ == '__main__':
    print(even_number_of_evens(5))
