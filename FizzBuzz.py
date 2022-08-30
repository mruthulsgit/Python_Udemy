print('''this is a simple program that is programmed  to do as if the numbers are divisible by fuzz then print 'fuzz' or the number is divisible by 
 buzz then print 'buzz' if the number is divisible by both the number then it has to print as 'fizzbuzz\'
 
 ''')
fizz = int(input('enter the number for fizz: '))
buzz = int(input('enter the number for buzz: '))
for i in range(1,100):
    if i % fizz == 0 and i % buzz == 0:
        print('fizzbuzz')
    elif i % fizz == 0:
        print('fizz')
    elif i % buzz == 0:
        print('buzz')
    else:
        print(i)