def sum(a,b):
    return a+b
sum(5,5)
'''
#questio 1
def recursive_factorial(n):
    if n == 0:  # Base case: if n equals 0
        return 1  # Return 1 (as 0! equals 1)
    else:  # If n is not equal to 0
        # Recursively call the function with n-1 as the argument and multiply the result by n
        return n * recursive_factorial(n-1)
    
#question 2
    def recursive_function(parameter):
    if base_case:
        # Return value for the base case

    else:
        # Recursive case: call the function with a simpler version of the problem
        recursive_function(simpler_parameter)

#question 3
    # Example of a call stack for a recursive function
recursive_function(3)
    recursive_function(2)
        recursive_function(1)
            recursive_function(0)
                return 1
            return 1 * 1
        return 2 * 1
    return 3 * 2

'''