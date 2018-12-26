import guess_num_game
import rand_zimu

print('请输入选择游戏\n1.数字游戏\n2.字母游戏')

game = eval(input('输入1或2：'))

if game == 1:
    game_num = guess_num_game.GuessNumGame()
    game_num.num_game(0,0,0)
elif game == 2:
    game_num = rand_zimu.GameLetter()
    game_num.letter_game()
else:
    print('别闹，输入错了')