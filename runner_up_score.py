if __name__ == '__main__':

    n = int(raw_input())

    arr = map(int, raw_input().split())

# uniq set
def uniq_list(arr):
    uniq_list = []

    for elem in arr:
        if elem not in uniq_list:
            uniq_list.append(elem)
    
    return uniq_list

            


uniq_list = uniq_list(arr)

arr.sort(resverse=True)

return arr[1]

