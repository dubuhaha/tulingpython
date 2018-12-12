
# 包含一个学生类
# 一个sayhello 函数
# 一个打印语句

class Student():
    def __init__(self, name="NoName", age =18):
        self.name = name
        self.age = age


    def say(self):
        print("My name is {}".format(self.name))


def sayHello():
    print("Hi, everybody, 欢迎学习python！")

print("我是模块p01呀，你喊我吗？")