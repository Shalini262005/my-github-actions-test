def factorial(n):
  """
  Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.

  Raises:
    ValueError: If n is a negative integer.
  """
  if not isinstance(n, int) or n < 0:
    raise ValueError("Factorial is only defined for non-negative integers")
  if n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result