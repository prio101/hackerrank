# https://www.hackerrank.com/challenges/exceptions/problem

if __name__ == '__main__':
    n = int(raw_input())
    input1 = raw_input()
    input2 = raw_input()
    
    inputs =[]
    inputs.append([int(input1),int(input2)])


class ZeroDivisionError:
  """Raised when the second argument of a division or modulo operation is zero"""

class ValueError:
  """Raised when the invalid literal for int() with base 10"""

print(inputs)

for item in inputs:
  for elem in item:
    print(elem)