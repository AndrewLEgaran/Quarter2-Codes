studnum = float(input("Enter the number of students: "))
subnum = float(input("Enter the number of subjects: "))
classavg = 0
for t in range(1, int(studnum)+1):
    print("Student", t)
    allscore = 0
    for k in range(1, int(subnum)+1):
        score = float(input("Enter score: "))
        allscore += score
    avg = allscore/subnum
    classavg += avg
    print("Average for Student", t, ":", avg)
print("Class Average:", classavg/studnum)