
import os

# Complete the solve function below.
def solve(s):
  splitted_txt = s.split(' ')
  capitalized_list = []

  for word in splitted_txt:
    capitalized_list.append(word.capitalize())
  
  print(' '.join(capitalized_list))

if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)
    

    
