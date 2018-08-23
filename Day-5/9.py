n = int(input())
student_marks = {}
for i in range(0,n):
    inputarray = input().split()
    scores = list(map(float,inputarray[1:]))
    student_marks[inputarray[0]] = sum(scores)/float(len(scores))
print("%.2f" % student_marks[input()])
    