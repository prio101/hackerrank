if __name__ == '__main__':
    N = int(raw_input())
    
    inputs =[]
    result = []

    for input in range(0, N):
      input = raw_input()
      inputs.append(input.split())
    
    result_list = []

    for item in inputs:
      temp_list = []
      action_name = item[0]
      temp_list = item.pop(0)

      if(action_name == 'insert'):
        result_list.insert(int(item[0]), int(item[1]))
      elif(action_name == 'remove'):
        result_list.remove(int(item[0]))
      elif(action_name == 'append'):
        result_list.append(int(item[0]))
      elif(action_name == 'pop'):
        if(len(result_list)>=1):
          result_list.pop()
      elif(action_name == 'reverse'):
        result_list.reverse()
      elif(action_name == 'sort'):
        result_list.sort()
      elif(action_name == 'print'):
        print(result_list)
      else:
       None
