# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

required_list = []
all_values = student_marks.values()

# searh the query name 
def SearchName(student_marks):
  for elem in student_marks:
    if(query_name == elem):
      required_list.append(student_marks[elem])

# get the avg for list total
def AvarageScore(required_list):
  length = len(required_list[0])
  sum_val = sum(required_list[0])

  return (sum_val / length)


SearchName(student_marks)

result = AvarageScore(required_list)

print("%.2f" % result)