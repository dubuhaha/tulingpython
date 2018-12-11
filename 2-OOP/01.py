'''
定义一个学生类，用来形容学生
'''
#定义一个空类
class Student():
    pass

#定义一个对象
mingyue = Student()

# 再定义一个类，用来面熟Python的学生
class PythonStudent():
    #None给不确定的值赋值
    name = None
    age = 18
    course = "Python"
    # 需要注意：
    # 1. def doHomework的缩进层级
    # 2. 系统默认有一个self参数。
    def doHoamework(self):
        print("I 在做作业")

        #推荐在函数末尾使用return语句
        return None

#实例化
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHoamework()
yueyue.__dict__
PythonStudent.__dict__