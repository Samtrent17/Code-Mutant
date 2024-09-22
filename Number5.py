#delivery services
#variables for Total amount and Amount paid
print('MBALE STORE DOCKERS')
totalamount = float(input('Please Enter Total Amount: '))
amutPaid = float(input('Please Enter Amount paid: '))
#check using if statement
if totalamount < 100000:
    print('Free Delivery')
else :
    DeliveryFee = 0.005*totalamount
    FinalSale = totalamount + DeliveryFee
    print('Delivery Fee: ', DeliveryFee, 'UGX')
    print('Final Sale Amount: ', FinalSale,'UGX')
    balance =amutPaid - FinalSale
    print('Balance: ', balance,'UGX')
    if balance > 0:
        print('Coming Right Up')
    else:
        print('Please Pay Some More')    
    