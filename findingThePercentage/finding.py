if __name__ == '__main__':
    n = int(input("How many students "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("name and scores ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("input name to query ")
    sums = 0
    try:
        for score in student_marks[query_name]:
            sums = sums + score
            print("{:0.2f}".format(sums/len(student_marks[query_name])))
    except:
        print("no such a name")
