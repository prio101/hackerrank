def wrap(string, max_width):
    result_list = []
    temp = 0
    length = len(string)

    for i in range(len(string)):
      result_list.append(string[temp:max_width])
      temp = i+max_width
    
    for paragraph in result_list:
      print(paragraph)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)