from random import random


import random
print('''This is a game called Rock Paper Scissors
the rules are mentioned below
1.you can choose one among the 3 item(Rock,Paper,Scissor)
2.Computer will also choose one among those by randomly
3.rock can beat scissor,scissors can beat paper and rock can beat scissor''')
print('\n\n Here the game begins\n 0 for scissor\t 1 for rock \t 2 for papers')
a = int(input())
com = random.randint(0,2)
print(com)
if a == 0 and com == 2:
    print('you won')
elif a > com:
    print('you won')
else:
    print('tie')
