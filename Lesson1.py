#Number 1
name = input('Enter your name: ')
print(f'Hello {name}')

#Number 2
num1 = int(input('Enter first digit: '))
num2 = int(input('Enter second digit: '))
print(f'Sum of Numbers is',num1+num2)
print(f'Difference of Numbers is',num1-num2)
print(f'Product of the Numbers is',num1*num2)
print(f'Result of remainder on Division',num1%num2)
print(f'Quotient of Numbers is',num1/num2)
print(f'Floor Division of Numbers is',num1//num2)


#Number 3
sentence = input('Enter sentence: ')
words = sentence.split()
print(len(words))


#Number 4
value = int(input('Enter the value: '))
if value % 2 ==0:
    print('Even')
else:
    print('Odd')

#Number 5
print(len(input('Enter your sentence: ')).split())