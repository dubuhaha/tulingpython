class GameLetter():
    def printA(self):
        # 打印字母A
        # 控制行
        for i in range(5):
            # 判断开始输入的位置
            for k in range(5-i):
                print(' ',end="")
            # 控制列
            for j in range(i + 1):
                if i == 0 or i == 2:
                    print("*", end=" ")
                elif j == 0 or j == i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # 打印B
    def printB(self):
        for i in range(2):
            for j in range(3):
                if i != 1:
                    if j < 2:
                        print("*", end=" ")
                elif j != 1:
                    if i != 0:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        for i in range(3):
            for j in range(3):
                if i != 1:
                    if j < 2:
                        print("*", end=" ")
                elif j != 1:
                    if i != 0:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # 打印C
    def printC(self):
        for i in range(5):
            for j in range(4):
                if i == 0 or i == 4:
                    if j == 0:
                        print(" ", end=" ")
                    else:
                        print("*", end=" ")
                elif j == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # 打印D
    def printD(self):
        for i in range(5):
            for j in range(4):
                if i == 0 or i == 4:
                    if j < 3:
                        print("*", end=" ")
                elif j == 0 or j == 3:
                    if i < 4:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    def letter_game(self):
        while 1:
            # 现在需要输入对应的字母，后续可以考虑ASCII码转字母，(97, 123)
            str = input("请输入一个你想要打印的字母（目前只能打印abcd),输入-1结束：")
            if str == '-1':
                break
            # 判断输入的字母
            elif str =='a':
                GameLetter.printA(self)
            elif str == 'b':
                GameLetter.printB(self)
            elif str == 'c':
                GameLetter.printC(self)
            elif str == 'd':
                GameLetter.printD(self)
            else:
                print('输入错误')

if __name__ == '__main__':
    game = GameLetter()
    game.letter_game()