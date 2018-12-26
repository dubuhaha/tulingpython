pw = 'abc123'
times = 3
while times:
    input_pw = input('请输入密码')

    if "*" in input_pw:
        print("密码中不能包括*")
    elif input_pw == pw:
        print("密码正确")
        break
    else:
        print("密码错误")
        times -= 1