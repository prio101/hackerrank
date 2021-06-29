import textwrap

def wrap(string, max_width):
    arr = textwrap.wrap(string, max_width)
    for x in range(len(arr)):
      if arr[x] is not None:
        arr[x]

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
