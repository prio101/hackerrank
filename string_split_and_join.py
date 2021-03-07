def split_and_join(line):
    split_list = line.split(" ")
    joined_str = "-".join(split_list)
    return joined_str
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print result