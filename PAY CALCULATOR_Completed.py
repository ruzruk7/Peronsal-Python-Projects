# PAY CALCULATOR 
#   by ruzruk7

# Pay Calcualtor provides how much you will earn in a paycheck.
# NOTE: Due to this program not being tailored to your companies payroll calculations, allow for some pay discrepency.->
#-> However you will get a decent idea of how much you will be earning in your coming paycheck.

##### INSTRUCTIONS #####
# 1) You will need to install python interpreter from https://www.python.org/downloads/.
# 2) Install VS code from https://code.visualstudio.com/download.
# 3) Copy everything in this file and paste it inside a VS code window.
# 4) Enter your hourly pay, bonus/incentive/overtime pay, tax percentage in decimal format, and the total amount of any differentials.
# 5) Save the file.
# 6) open the file using the python interpretor and calcualate away!

##### ENTER THESE AMOUNTS #####
hourly_pay = 00.00   # Enter in your hourly pay rate

bonus_pay = 00.00   # Enter your bonus/incentive/overtime rate or any other type of additional rate adds on top of your hourly-pay   

total_tax_deduction = 00.00    # Take the percentage of Tax that is deducted and turn it into decimal format. 
# NOTE: Due to differences in state-income tax, a difinitive percentage cannot be provided. ->
# Calculate the percentage of tax that was reduced from your last 3 paychecks ->
# and enter the percentage that is most consistantly deducted.


sum_of_differentials = 0  # Enter the sum total of differentials added. 
# NOTE: because differentials in companies are calculated based on different methods -> 
# Pay Calculator only adds the sum of the differentials (YOU calculate and provide) to your base pay.
# NOTE: For sake of more accurate representation of actual pay I suggest keeping this as 0, whatever you earned in differentials are just a cherry on top but not the main cake.






import math
class Pay_calculator:
    totals = []
    print('Welcome to the pay calculator. Enter "q" at anytime to exit.')

    while True:
        nam = input('How many hours did you work: ')
        if nam == 'q':
            break
        if nam == 'r':
            totals.clear()
            print('Restarting Pay Calculator\n')
            continue
        bn = input('Is it a bonus shift? Enter 1 for normal shift and 2 for bonus shift:\nInput: ')
        if bn == 'r':
            totals.clear()
            print('Restarting Pay Calculator')
            continue
        if bn == 'q':
            break
        bnn = float(bn)
        if bnn == 1:
            bp=(float(nam) * hourly_pay)
            mintx=(bp * total_tax_deduction)
            urp=(bp-mintx)
        if bnn == 2:
            bp=(float(nam) * bonus_pay)
            mintx=(bp * total_tax_deduction)
            urp=(bp-mintx)
        if sum_of_differentials != 0:
            tax_amount = (urp + float(sum_of_differentials) * total_tax_deduction)
            sum_post_tax = ((urp + float(sum_of_differentials)) - tax_amount)
            totals.append(sum_post_tax)
        else:
            totals.append(urp)
        print('Pay = ', urp)
        z = input('\nEnter "=" to see sum total of all paychecks.\nEnter "r" to reset calculation.\nPress "Enter" to add another amount.\nPress "a" to add an amount:\ninput: ')
        if z == "=":
                x = math.fsum(totals)
                print(f'Total pay is: {x}')
        if z == 'q':
            break
        if z == 'r':
            totals.clear()
            print('Restarting Pay Calculator\n')
            continue
        if z == 'a':
            a = input('Amount: ')
            totals.append(int(a))
        else:
            print('Restarting Pay Calculator\n')
            continue

pc = Pay_calculator


