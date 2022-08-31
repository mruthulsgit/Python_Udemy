import random
print('''This program is to generate a random password with your criterias''')
alphabets = ['a','b','c','d','e','f','g','h','i',
        'j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z']

symbols = ['@','$','!','%','&','*','(',')','-','_','+','=']
numbers = ['0','1','2','3','4','5','6','7','8','9']
no_alphabets = int(input('enter the no of alphabets :')) #here you can give how many alphabets for your passwd
no_symbols = int(input('enter the no of symbols :')) #here you can give how many symbols for your passwd
no_numbers = int(input('enter the no of numbers :')) #here you can give how many numbers for your passwd
pass_list = []
for alp in range(no_alphabets):
    pass_list.append(random.choice(alphabets))
for symbol in range(no_symbols):
    pass_list.append(random.choice(symbols))
for num in range(no_numbers):
    pass_list.append(random.choice(numbers))
random.shuffle(pass_list)
password =''
for i in pass_list:
    password += i
print(password)


