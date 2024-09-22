attendance = int(input('Enter attendence: '))
if attendance >=60:
    print('Successful')
    course_work_mark = float(input('Enter Course work mark out 50: '))
    if course_work_mark >= 17.5:
        print('Permitted to do Exam')
        exm_mark = float(input('Enter Exam mark out of 50: '))
        if exm_mark >= 17.5:
            print('Allowed to move to Year 1 Semester 2')
            print('Congratulations, you have passed.')
        else:
            print('Unable to continue to Year 1 Semester 2')
    else:
        print('Unable to do Exam')
else:
    print('Unsuccessful')