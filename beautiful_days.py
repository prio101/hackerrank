# URL: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true


def beautiful_days(i, j, k):
  date_range = range(i,j+1)
  for item in date_range:
    print(item)
  


def main():
  i = 20 # start day
  j = 23 # end day
  k = 6 # divisable

  beautiful_days(i, j, k)


if __name__ == '__main__':
  main()