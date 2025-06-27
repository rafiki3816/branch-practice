def fibonacci_recursion(n):
  """
  재귀 함수를 사용하여 n번째 피보나치 수를 계산합니다.

  Args:
    n: 계산할 피보나치 수의 위치 (0 이상의 정수).

  Returns:
    n번째 피보나치 수.
  """
  if n <= 1:
    return n
  else:
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

print(fibonacci_recursion(4))
