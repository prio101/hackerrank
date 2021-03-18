def count_substring(string, sub_string):
    found_list = []
    found_indices = []
    found_indices.append(string.index(sub_string))
    print(found_indices)
    return len(found_list)


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create LPS[] that will hold the longest prefix suffix
    # values for the pattern

    lps = [0]*M
    j = 0 # index for pat[]


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)