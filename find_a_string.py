def count_substring(string, sub_string):
    found_list = []
    found_indices = []
    found_indices.append(string.index(sub_string))
    print(found_indices)
    return len(found_list) 


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)