def count_substring(string, sub_string):
    found_list = []
    found_list.append(string.find(sub_string))

    return len(found_list)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)