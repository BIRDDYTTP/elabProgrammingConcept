grade_list = []
cradit_list = []
while True:
    grade = float(input('Grade input : '))
    cradit = float(input('Cradit input : '))
    if grade < 0 or cradit < 0:
        break
    else:
        grade_list.append(grade)
        cradit_list.append(cradit)
summary_list = []
for x in range(len(grade_list)):
    summary = grade_list[x] * cradit_list[x]
    summary_list.append(summary)
print('GPA is %.2f' %(sum(summary_list)/sum(cradit_list)))