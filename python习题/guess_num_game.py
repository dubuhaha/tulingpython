import random
import math

'''
输入一个三位数与程序随机数比较大小：
1. 如果大于程序随机数，则分别输出这个三位数的个位、十位、百万
2. 如果等于程序随机数，则提示中奖，记100分
3. 如果小于程序随机数，则将12个字符输入到文本文件中
    （规则是每一条字符串长度为12，单独占一行，并且前四个是字母，后8个是数字）
'''
class GuessNumGame():
    def line(self):
        # 定义一个空字符串用于拼接数字
        str_num = ''
        # 循环前四个随机字母（用ASCII对应的值来随机在转换为字母）
        for i in range(4):
            # 随机小写字符ASCII码值
            num = random.randrange(97, 123)
            # 将ASCII码值转换成对应的字母
            str_s = chr(num)
            # 依次拼接得到的随机字母
            str_num = str_num + str_s
        # 循环后8个随机数字
        for i in range(8):
            num = random.randrange(0,10)
            str_num = str_num+str(num)
        return str_num


    def num_game(self, score, total):
        while 1:
            # 输入函数
            num = eval(input("请输入一个三位数,输入-1结束："))
            if num == -1:
                break
            # 程序随机数
            rd_num = random.randrange(100,1000)

            if 100 <= int(num) <= 999:# 输入函数输入的是字符类型，不强制转换会报错
               # 计算有效输入次数
               total += 1
               print("输入第%d次"%total)
               if num > rd_num:
                   gw = num%10
                   sw = num%100//10
                   bw = num//100
                   print("程序随机数字是{}".format(rd_num))
                   print("您的猜的数字是-->百位：{}，十位：{}，个位：{}".format(bw,sw,gw))
               elif num < rd_num:
                   print("程序随机数字是{}".format(rd_num))
                   # 由于120个字符需每行12个可以知，需要重复10次
                   for i in range(10):
                       str_line = GuessNumGame.line(self)
                       print(str_line)
                       # 执行文件出入操作
                       with open('str_num.txt', 'a') as f:
                           f.write(str_line + '\n')
               elif num == rd_num:
                   score += 100
                   print("程序随机数字是{}".format(rd_num))
                   print("恭喜你猜对了，加100分！，现在分数是%d"%score)
            else:
                print("请按规定输入！")

# 程序入口
if __name__ =='__main__':
    # 定义一个变量存储分数
    score = 0
    # 定义一个变量用于计算累计输入此时
    total = 0
    # 直接类名调用
    # GuessNumGame.num_game(0, score, total)
    # 实例化类后调用
    game = GuessNumGame()
    game.num_game(score,total)