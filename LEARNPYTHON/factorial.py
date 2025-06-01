#Lambda
from functools import reduce

# Factorial using lambda
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))

# Compute factorial of 5
result = factorial(5)

# Print using string concatenation
print("The factorial of 5 is " + str(result))
