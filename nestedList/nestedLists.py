if __name__== '__main__':
    stu = []
    pythonStu = []
    for _ in range(int(input("How many students"))):
        name = input("Name: ")
        score = float(input("Score: "))
        single = [name,score]
        pythonStu.append(single)

    pythonStu=sorted(pythonStu, key=lambda stud: (stud[1]))
    minim = pythonStu[0][1]
    i = 0
    while pythonStu[i][1] == minim:
        if i < (len(pythonStu)-1):
            i += 1
        else:
            print("No second Students")
            exit(0)

    secondmin=pythonStu[i][1]

    while pythonStu[i][1]==secondmin:
            stu.append(pythonStu[i][0])
            if i < (len(pythonStu)-1):
                i += 1
            else:
                break

    stu.sort()
    print('Seconds: ')
    for name in stu:
        print(name)
