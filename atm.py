def ATM():
    print('transaction in progress')# transaction in progress displays immediately user inserts he's/her credit card
    print('OGBE OSEMUDIAME PHILLIP welcome to first bank of nigeria ')
    password=int(1234)
    user_password=int(input('enter the four digit password: '))
    if user_password==password:
        user_first=int(input('choose the transaction you want\n(1)savings \n(2)current\n: '))
        if user_first==1 or user_first==2:
            display_receipt=int(input('do you want a receipt \n(1)YES \n(2)NO: '))
            if display_receipt==1 or 2: # receipt will be printed,else receipt will nnever be printed
                user_next_1=int(input('choose the options for your tansactions \n(1)withdraw \n(2)buy airtime \n(3)pay bills \n(4)transfer funds\n: ')) 
                if user_next_1==1:
                    user_stage_1=int(input('enter the amount you want \n(1)500 \n(2)1000 \n(3)2000 \n(4)10000 \n(5)20000 \n(6)OTHERS: '))
                    if user_stage_1==1 or user_stage_1==2 or user_stage_1==3 or user_stage_1==4 or user_stage_1==5:
                        print('transaction in progress')
                        print('please take your cash')
                        user_stage_2=input('do you still want to perform another transaction \n(1)yes \n(2)no\n? ')
                        if user_stage_2=='1':
                            return ATM()
                        else:
                             print('thank you')
                    elif user_stage_1==6:
                        amount=int(input('enter the amount in multiple of 1000: '))
                        print('transaction in progress')
                        print('please take your cash')
                        user_stage_2=input('do you still want to perform another transaction \n(1)yes \n(2)no\n? ')
                        if user_stage_2=='1':
                            return ATM()
                        else:
                             print('thank you: ')# receipt comes out from machine,else it will never come
                elif user_next_1==2:
                    user_stage_2=int(input('what network do you want to recharge \n(1)AIRTEL\n(2)9MOBILE\n(3)MTN\n(4)GLO\n(5)VISAFONE? '))
                    if user_stage_2==1 or 2 or 3 or 4 or 5:
                        choose_amount=int(input('enter the amount you want \n(1)500 \n(2)1000 \n(3)2000 \n(4)10000 \n(5)20000 \n(6)OTHERS\n: '))
                        if choose_amount==1 or choose_amount==2 or choose_amount==3 or choose_amount==4 or choose_amount==5:
                            user_phoneNumber=int(input('enter the phone number: '))
                            print('transaction in progress')
                            print('transaction sucessful')
                            user_stage_2=input('do you still want to perform another transaction \n(1)yes \n(2)no\n? ')
                            if user_stage_2=='1':
                                return ATM()
                            else:
                                 print('thank you')# receipt comes out from machine,else it will never come
                        elif choose_amount==6:
                            amount2=int(input('enter the amount in multiples of 1000: '))
                            user_phoneNumber=int(input('enter the phone number: '))
                            print('transaction in progress')
                            print('transaction sucessful')
                            user_stage_2=input('do you still want to perform another transaction \n(1)yes \n(2)no\n? ')
                            if user_stage_2=='1':
                                return ATM()
                            else:
                                 print('thank you')# receipt comes out from machine,else it will never come
                elif user_next_1==3:
                    user_stage_3=int(input('which bills do you wish to pay \n(1)CABLE TV \n(2)NEPA BILLS \n(3)BET 9JA? '))
                    if user_stage_3==1:
                        options=int(input('choose the cable options \n(1)DSTV \n(2)GOTV \n(3)STARTIMES \n(4)TSTV: '))
                        if options==1 or 2 or 3 or 4:
                            option2=int(input('enter the amount you wish to subscribe for \n(1)1800\n(2)3500\n(3)5000\n(4)15000\n: '))
                            account_number=input('enter the smart_card number/account: ')
                            print('transaction in progress')
                            print('transaction sucessful')
                            user_stage_2=input('do you still want to perform another transaction \n(1)yes \n(2)no\n? ')
                            if user_stage_2=='1':
                                return ATM()
                            else:
                                 print('thank you')# receipt comes out from machine,else it will never come
                    elif user_stage_3==2:
                        prepaid_number=int(input('enter prepaid number: '))
                        amount=int(input('enter the amount you want \n(1)1000 \n(2)2000 \n(3)5000 \n(4)10000 \n(5)20000\n: '))
                        if amount==1 or 2 or 3 or 4 or 5:
                            print('transaction in progress')
                            print('transaction sucessful')
                            user_stage_2=input('do you still want to perform another transaction \n(1)yes \n(2)no\n? ')
                            if user_stage_2=='1':
                                return ATM()
                            else:
                                print('thank you')# receipt comes out from machine,else it will never come
                    elif user_stage_3==3:
                        account_name=input('what is your bet 9ja user name? ')
                        amount_todo=int(input('enter the amount you wish to pay: '))
                        print('transaction in progress')
                        print('transaction sucessful')
                        user_stage_2=input('do you still want to perform another transaction \n(1)yes \n(2)no\n? ')
                        if user_stage_2=='1':
                            return ATM()
                        else:
                             print('thank you')# receipt comes out from machine,else it will never come
                elif user_next_1==4:
                    user_option=int(input('choose options for transfer \n(1)INTER BANK TRANSFER \n: '))
                    if user_option==1:
                        bank_choice=int(input('which bank do you wish to transfer to \n(1)ACCESS \n(2)DIAMOND \n(3)GTB \n(4)UNION \n(5)STANDBIC \n(6)FIRST \n(7)OTHERS\n: '))
                        if bank_choice==1 or bank_choice==2 or bank_choice==3 or bank_choice==4 or bank_choice==5 or bank_choice==6:
                            account=int(input('choose debitors account \n(1)SAVINGS \n(2)CURRENT: '))
                            if account==1 or 2:
                                account_num=int(input('enter the account number you would like to transfer to: '))
                                print('FISAYO OLUWATOBILOLA DANIEL')# creditors account name is displayed
                                amount=int(input('enter the amount in multiples of 1000: '))
                                account2=int(input('choose the  creditors account \n(1)SAVINGS \n(2)CURRENT: '))
                                if account2==1 or 2:
                                    print('transaction in progress')
                                    print('transaction sucessful')
                                    user_stage_2=input('do you still want to perform another transaction \n(1)yes \n(2)no\n? ')
                                    if user_stage_2=='1':
                                        return ATM()
                                    else:
                                        print('thank you')# receipt comes out from machine,else it will never come
                        elif bank_choice==7:
                            bank_choice2=int(input('which bank do you wish to transfer to \n(1)FIDELITY \n(2)FCMB \n(3)ECO \n(4)SKY \n(5)ZENITH \n(6)BACK: '))
                            if bank_choice2==1 or bank_choice2==2 or bank_choice2==3 or bank_choice2==4 or bank_choice2==5:
                                account=int(input('choose the debitors account \n(1)SAVINGS \n(2)CURRENT: '))
                                if account==1 or 2:
                                    account_num=int(input('enter the account number you would like to transfer to: '))
                                    print('FISAYO OLUWATOBILOLA DANIEL')# creditors account name is displayed
                                    amount=int(input('enter the amount in multiples of 1000: '))
                                    account2=int(input('choose the  creditors account \n(1)SAVINGS \n(2)CURRENT: '))
                                    if account2==1 or 2:
                                        print('transaction in progress')
                                        print('transaction sucessful')
                                        user_stage_2=input('do you still want to perform another transaction \n(1)yes \n(2)no\n? ')
                                        if user_stage_2=='1':
                                            return ATM()
                                        else:
                                            print('thank you')# receipt comes out from machine,else it will never come
                            elif bank_choice2==6:
                                bank_choice=int(input('which bank do you wish to transfer to \n(1)ACCESS \n(2)DIAMOND \n(3)GTB \n(4)UNION \n(5)STANDBIC \n(6)FIRST \n(7)OTHERS\n: '))
                                if bank_choice==1 or bank_choice==2 or bank_choice==3 or bank_choice==4 or bank_choice==5 or bank_choice==6:
                                    account=int(input('choose debitors account \n(1)SAVINGS \n(2)CURRENT: '))
                                    if account==1 or 2:
                                        account_num=int(input('enter the account number you would like to transfer to: '))
                                        print('FISAYO OLUWATOBILOLA DANIEL')# creditors account name is displayed
                                        amount=int(input('enter the amount in multiples of 1000: '))
                                        account2=int(input('choose the  creditors account \n(1)SAVINGS \n(2)CURRENT: '))
                                        if account2==1 or 2:
                                            print('transaction in progress')
                                            print('transaction sucessful')
                                            user_stage_2=input('do you still want to perform another transaction \n(1)yes \n(2)no\n? ')
                                            if user_stage_2=='1':
                                                return ATM()
                                            else:
                                                print('thank you')# receipt comes out from machine,else it will never come
                             
    else:
        print('wrong password')
        return ATM()
print(ATM())

