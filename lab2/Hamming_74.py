code = input('Here: ')
code = '0'*(7-len(code)) + code
s1, s2, s3 = sum([int(code[0]), int(code[2]), int(code[4]), int(code[-1])]) % 2, \
                   sum([int(code[1]), int(code[2]), int(code[-2]), int(code[-1])]) % 2, \
                   sum([int(code[-4]), int(code[-3]), int(code[-2]), int(code[-1])]) % 2

error = int(str(s3)+str(s2)+str(s1), 2)
if error == 0:
    print('Evrything is correct!')
    print(code, 'in binary system')
    print(int(code, 2), 'in decimal system')
else:
    code = code[:error-1] + str((int(code[error-1]) + 1) % 2) + code[error:]
    print('There is error in', error, 'position. Right one is: ')
    print(code, 'in binary system')
    print(int(code, 2), 'in decimal system')
