def BubbleSort(arr_list):
  length =  len(arr_list)
  tempo = []

  # sorting by reverse order by score and then alphabettically
  # Input : [["name: string", "score: int"]]

  for i in range(0,length):
    for j in range(0, (length - i) - 1 ):
      if(arr_list[j][1] < arr_list[j+1][1]):
        tempo = arr_list[j]
        arr_list[j] = arr_list[j+1]
        arr_list[j+1] = tempo

    for j in range(0, (length-i) - 1):
      if(arr_list[j][1] == arr_list[j+1][1]):
        tempo = arr_list[j]
        if(arr_list[j][0] > arr_list[j+1][0]):
          arr_list[j] = arr_list[j+1]
          arr_list[j+1] = tempo
  
  return arr_list