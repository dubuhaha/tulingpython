#借助于importlib包可以实现导入已数字开头的模块名称
import importlib

# 相当于导入了一个叫01的模块并把导入的模块赋值给了tuling变量
tuling = importlib.import_module("01")

stu = tuling.Student("xiaojing", 19)

stu.say()