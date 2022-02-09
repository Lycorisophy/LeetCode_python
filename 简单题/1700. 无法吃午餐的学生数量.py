def countStudents(students:  [int], sandwiches: [int]) -> int:
    cnt0, cnt1 = 0, 0
    for student in students:
        if student == 1:
            cnt1 += 1
        else:
            cnt0 += 1
    while students:
        student = students.pop(0)
        sandwiche = sandwiches[0]
        if student == sandwiche:
            sandwiches.pop(0)
            if student == 1:
                cnt1 -= 1
            else:
                cnt0 -= 1
        else:
            if student == 1:
                if cnt0 == 0:
                    return cnt1
            else:
                if cnt1 == 0:
                    return cnt0
            students.append(student)
    return 0


if __name__ == '__main__':
    print(countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
    print(countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))
    print(countStudents([1], [0]))

