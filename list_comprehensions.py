if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

from itertools import combinations    


arr = x, y, z
r = n

unfiltered_list = []

unfilterd_lists = list(combinations(arr, 3))

print(unfilterd_lists)

