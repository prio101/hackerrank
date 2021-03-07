def swap_case(s):
    length_str = len(s)
    list_str = s.split()
    new_str_list = []
    
    for word in list_str:
      for char in word:
        if(char.isupper()):
          new_str_list.append(char.lower())
        elif(char.islower()):
          new_str_list.append(char.upper())        
        else:
          new_str_list.append(char)
      new_str_list.append(" ")     
    return ''.join(new_str_list)
    
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)