
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
        # we can code out the lines below as evens = 0 covers that
        # if numbers == []:
        #     return False
        # else:
        evens = sum([1 for n in numbers if n % 2 == 0])
        """
        evens equal the sum of 1 for each even number ex. [1,2,3,4,]
        evens would equal 2 (2,4 are even number therefore, 1 + 1)
        """

        # we could replaced code below with the code above
        # by changing evens == 0 to the sum of ones for each even number
        # for n in numbers:
        #     if n % 2 == 0:
        #         evens += 1
        return True if evens and evens % 2 == 0 else False
        """
        code above return true if evens not equal zero (True) and evens modulus
        2 eqaul 0 (even numbers) else return False
        """
        # if evens:
        #     return evens % 2 == 0
        # else:
        #     return False
    else:
        raise TypeError("A list was not passed into the function")


# this allows us to limit this function to be run only when is called
# in this file, with command python3 evens.py
# it won't be called if the function is called in other file


if __name__ == '__main__':
    print(even_number_of_evens([2, 1, 4]))
