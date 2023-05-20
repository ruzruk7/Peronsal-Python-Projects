# PAY CALCULATOR 

# Pay Calcualtor provides how much you will earn in a paycheck and has a mini calculator mode to help wage calcualtions and bills
# NOTE: Due to this program not being tailored to your companies payroll calculations, allow for some pay discrepency.->
#-> However you will get a decent idea of how much you will be earning in your coming paycheck.

##### ENTER THESE AMOUNTS #####
hourly_pay = 0  # Enter in your hourly pay rate

bonus_pay = 0   # Enter your bonus/incentive/overtime rate or any other type of additional rate adds on top of your hourly-pay   
total_deduction = 0    # Take the percentage of Tax that is deducted and turn it into decimal format. 
# NOTE: Due to differences in state-income tax, a difinitive percentage cannot be provided. ->
# Calculate the percentage of tax that was reduced from your last 3 paychecks ->
# and enter the percentage that is most consistantly deducted.

sum_of_differentials = 0  # Enter the sum total of differentials added. 
# NOTE: because differentials in companies are calculated based on different methods -> 
# Pay Calculator only adds the sum of the differentials (YOU calculate and provide) to your base pay. ->





import math
class Pay_calculator:

    totals = []
    calc_list = []
    while True:
        print('Welcome to the pay calculator. Enter "q" at anytime to exit.\n')
        mode = (input('Would you like to enter Wage calculater mode or Normal calculator mode? press \'W\' for Wage calculator\npress \'C\' for Calcualtor mode\n')).lower()
        if mode == 'c':
            print('Welcome to CALCULATOR MODE.\n')
            while True:
                q = input('Enter problem as 0000 action 0000: ').strip(' ')
                calc_list.append(q.split())
                try:
                    first = calc_list[0][0][0]
                    action = calc_list[0][0][1]
                    second = calc_list[0][0][2]
                    if action == '+':
                        quot = float(first) + float(second)
                        print(f"{first} {action} {second} = {quot}")
                        calc_list.clear()
                        continue
                    if action == '*':
                        quot = float(first) * float(second)
                        print(f"{first} {action} {second} = {quot}")
                        calc_list.clear()
                        continue
                    if action == '-':
                        quot = float(first) - float(second)
                        print(f"{first} {action} {second} = {quot}")
                        calc_list.clear()
                        continue
                    if action == '/':
                        quot = float(first) / float(second)
                        print(f"{first} {action} {second} = {quot}")
                        calc_list.clear()
                        continue
                except:
                    if q == 'q' or '':
                        print("returning to main menu...\n")
                        break
        if mode == 'w':
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
                    mintx=(bp * total_deduction)
                    urp=(bp-mintx)
                if bnn == 2:
                    bp=(float(nam) * bonus_pay)
                    mintx=(bp * total_deduction)
                    urp=(bp-mintx)
                if sum_of_differentials != 0:
                    tax_amount = (urp + float(sum_of_differentials) * total_deduction)
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
        if mode == 'q':
            break
        else:
            continue
    

pc = Pay_calculator


