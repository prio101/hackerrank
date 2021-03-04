arr = []

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())

    arr.append([name, score])
    sorted_list = []

def BubbleSort(arr_list):
  length =  len(arr_list)
  tempo = []

  # sorting by order by score and then alphabettically
  # Input : [["name: string", "score: int"]]

  for i in range(0,length):
    for j in range(0, (length - i) - 1 ):
      if(arr_list[j][1] > arr_list[j+1][1]):
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

# From Sorted List With Possible Cloned Element

def SecondMax(arr_list):
  min_val = arr_list[0][1]
  second_min_val = 0
  new_list = []
  result_list = []
  
  for item in arr_list:
    if item[1] != min_val :
      new_list.append(item)

  second_min_val = new_list[0][1]

  for item in new_list :
    if item[1] == second_min_val:
      result_list.append(item)
  
  return result_list


sorted_list = BubbleSort(arr) 

result_list = SecondMax(sorted_list)

# printing the names from nested list
for item in result_list:
  print(item[0])