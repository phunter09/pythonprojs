def nric_check(nric, alpha):
    weight = (2, 7, 6, 5, 4, 3, 2)
    conversion = ('A','B','C','D','E','F','G','H','I','Z','J')
    sum = 0
    count = 0
    for i in nric[1:8]:
        sum += (int(i) * weight[count])
        count += 1
    remainder = sum%11
    check = 11 - remainder
    if alpha == conversion[check - 1]:
        print(True)
    else:
        print(False)
