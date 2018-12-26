'''
创建北京和成都两个校区
创建Linux和Python两个课程
创建北京校区的Python3期课程和成都校区的Linux1期课程
管理员创建了北京校区的学员小张，并将其分配在Python3期
管理员创建讲师小周，并将其分配给Python3期
讲师小周创建了一条Python3期的上课记录Day02
讲师小周为Day02这节课所有的学员批改了作业，小张得了A，小王得了B
学员小张查看了自己所报的课程
学员小张在查看了自己的Python3的成绩列表后退出了
学员小张给了讲师小周好评
'''

Course_list = [] # 存储学校开设的课程

# 定义一个学校类
class School():
    def __init__(self, school_name):
        self.school_name = school_name
        self.students_list = []
        self.teachers_list = []

        global Course_list

    def hire(self, obj):
        self.teachers_list.append(obj.name)
        print("我们招聘了一个老师{}".format(self.obj.name))

    def enroll(self, obj):
        self.students_list.append(obj.name)
        print("我们招收了一个新学员{}".format(obj.name))

# 年级类，是School类的子类
class Grade(School):
    def __init__(self, school_name, grade_code, grade_course):
        super(Grade, self).__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        Course_list.append(self.course)

        print("我们现在有了{}学习{}年级的{}课程".format(self.school_name, \
                                           self.code, self.course))

    def course_info(self):
        print("课程大纲{}是 day01, day02, day03".format(self.course))

# 学校成员类父类
class School_members():
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []

        print("我叫{}，我是一个{}".format(self.name, self.role))

# 学生类-School_members的子类
stu_num_id = 00  # 学号初始值
class Students(School_members):
    def __init__(self, name, age, sex, role, course):
        super(Students, self).__init__(name, age, sex, role)
        global stu_num_id
        stu_num_id += 1
        # 拼接学号
        stu_id = course.school_name + 'S' + str(course.code) + \
            str(stu_num_id).zfill(2)

        self.id = stu_id
        self.mark_list = {} # 成绩表，存储学生课程成绩

    def study(self, course):
        print("我来这里学习{}课程，我的学号是{}".format(course.course, self.id))

    def pay(self, course):
        print("我交钱报名{}课程了".format(course.course))
        # 将报名的课程添加到该学生的课程列表
        self.course_list.append(course.course)

    # 给老师评价
    def praise(self, obj):
        print("{}觉得{}的课程真棒，五星好评".format(self.name, obj.name))

    # 查看课程成绩
    def mark_check(self):
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("我查完了，退出")

# 老师类，School_members的子类
th_num_id = 00  # 老师初始编号
class Teachers(School_members):
    def __init__(self, name, age, sex, role, course):
        super(Teachers, self).__init__(name, age, sex, role)
        global th_num_id
        # 拼接老师id
        th_id = course.school_name + "T" + str(course.code) + \
            str(th_num_id).zfill(2)
        self.id = th_id

    def teach(self, course):
        print("我来这里讲{}课程，我的id是{}".format(course.course, self.id))

    # 课程评分方法
    def record_mark(self, date, course, obj, level):
        obj.mark_list["Date" + date] = level

# 测试代码
# 创建python和Linux课程
Python = Grade("BJ","3", "Python")
Linux = Grade("CD", "1", "Linux")
print(Course_list)
print('=' * 20)

# 创建一个学生小张
a = Students("小张",18,"male","student",Python)
Python.enroll(a) # 注册
a.pay(Python)
a.study(Python)
print('=' * 20)


b = Students("小王",20,"female","student",Python)
Python.enroll(b)
b.pay(Python)
b.study(Python)
print('=' * 20)

# 创建老师，周老师
t = Teachers("周老师",28,"male","teacher",Python)
Python.enroll(t)
t.teach(Python)
# 给学生打分
t.record_mark('01',Python,a,'B')
t.record_mark('02',Python,a,'A')
t.record_mark('01',Python,b,'A')
t.record_mark('02',Python,a,'S')

print("小王查看了自己的课程")
print(b.course_list)
print("小王查看了自己的成绩")
b.mark_check()
print("小王退出了")
b.out()
print("=" * 20)
print("各个好评啊")
a.praise(t)