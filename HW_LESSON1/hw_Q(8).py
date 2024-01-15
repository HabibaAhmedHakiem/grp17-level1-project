# assignment (8)
import math
loan_amount = 100000
Monthly_Intrest_rate = 0.01
No_Years = 7
x = 1 + Monthly_Intrest_rate
y = No_Years * 12
Monthly_payment = ( loan_amount * Monthly_Intrest_rate ) / ( 1 - (1 / (math.pow(x,y))) )
Monthly_payment = round( Monthly_payment,2 )
print('monthly payment is', Monthly_payment )
Total_Payment = Monthly_payment * No_Years * 12
print('total payment is', Total_Payment )
