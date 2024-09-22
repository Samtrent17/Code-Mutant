print('UGANDA VOTING SYSTEM')
#Age from voting
vote = int(input('Please Enter the Age: '))

#Registration for being a voter
#variable for citizenship
print('1.Ugandan')
print('2.Non Ugandan')
citizenship = int(input('Enter your Citizenship: '))
#checking using if statement
if vote > 18 and citizenship == 1:
    print('Allowed to Proceed.')
    print('1.Registered')
    print('2.Not Registered')
    registration = int(input('Citizen registerd for voting: '))
    if registration == 1 :
        print('Congratulations, You are Eligible to vote.')
    elif registration == 2 :
        print('You are not welcome to vote.')
else:
    print('Could be allowed to proceed.')
