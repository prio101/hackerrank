if __name__ == '__main__':
    N = int(raw_input())
    
    inputs =[]
    
    for input in range(0, N):
      input = raw_input()
      inputs.append(input.split())

    print(inputs)
    
    result_list = []

    for item in inputs:
      temp_list = []
      action_name = item[0]
      temp_list = item - item[0]

      if(action_name == 'insert'):
        result_list.insert(temp_list)
      elif(action_name == 'remove'):
        result_list.remove(temp_list)
      elif(action_name == 'append'):
        result_list.append(temp_list)
      elif(action_name == 'pop'):
        result_list.pop(temp_list)
      elif(action_name == 'reverse'):
        result_list.reverse()
      elif(action_name == 'sort'):
        result_list.sort()
      elif(action_name == 'print'):
        print(result_list)
      else
        return None