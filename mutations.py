def mutate_string(string, position, character):
    list_str = list(string)
    list_str[position] = character
    string = ''.join(list_str)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new