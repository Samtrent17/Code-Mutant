#ask the user for the temperature
temp = float(input('Please Enter the Temperature in Entebbe: '))
#checking using if 
if temp > 30:
    print('Hot')
elif  20 <temp < 30:
    print('Warm')
elif temp < 20:
    print('Cool')
