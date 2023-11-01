class Bank:
    def __init__(self) -> None:
        self.name = 'admin'
        self.bank_balance=0
        self.total_loans=0
        self.accounts=[]
        self.is_bankrup=False
        self.loan_feature=False

    def creat_an_account(self, account):
        flag = True
        for ac in self.accounts:
            if ac == account:
                flag=False
        if flag:
            self.accounts.append(account)
        else:
            print('\n An account exist with same data')
    
    def deleted_an_account(self, account_number):
        flag = True
        for ac in self.accounts:
            if ac.account_number == account_number:
                self.accounts.remove(ac)
                flag = False
                break
        if flag:
            print(f'Invalid account number {account_number}\n')
        
    def check_all_account(self):
        for accs in self.accounts:
            print(f'Account Holder Name: {accs.name} AC Number {accs.account_number} AC Type: {accs.account_type}\n')

    def check_total_bank_balance(self):
        print(f'Total Bank Balance is {self.bank_balance}\n')
    
    def check_total_loan(self):
        print(f'Total loan is {self.total_loans}\n')
    
    def loan_feature(self, bool):
        self.loan_feature=bool
    
    def loan_request(self, amount):
        if self.is_bankrup:
            return(False, 'The bank is brankrup\n')
        elif self.loan_feature:
            return(False, 'Loan feature is off\n')
        else:
            if amount <= self.bank_balance:
                self.bank_balance -=amount
                self.total_loans+=amount
                return(True, f'You successfully get ${amount} loan\n')
            else:
                return(False, 'Bank does not have that enough Money')


class Account:
    def __init__(self, name, email, address, type) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.account_type=type
        self.balance=0
        self.account_number = f'{self.name}-{self.email}-{self.address}'
        self.loan_limit=2
        self.transaction_history=[]

    def diposit(self, bank, amount):
        if bank.is_bankrup:
            print('This Bank is Bankrupt\n')
            return
        if amount > 0:
            self.balance+=amount
            self.transaction_history.append(f'Diposit $ {amount} on AC Number {self.account_number} and Current balance is ${self.balance}')
            print(f'You diposit $ {amount} and total amount is $ {self.balance}')
        else:
            print('Input amount is Invalid!\n')
    
    def withdraw(self, bank, amount):
        if bank.is_bankrup:
            print('This Bank is Bankrupt\n')
            return
        if amount <= self.balance:
            self.balance-=amount
            self.transaction_history.append(f'Withdrawl amount ${amount} on AC Number {bank.account_number} and Current balance is ${self.balance}')
            print(f'Withdrawl amount ${amount} on AC Number {bank.account_number} and Current balance is ${self.balance}\n')
        else:
            print('Insufficient Balance\n')
    
    def check_available_balance(self):
        print(f'Your Total Balance is ${self.balance}')
    

    def check_transaction_history(self):
        flag = True
        for tranHis in self.transaction_history:
            flag = False
            print(tranHis)
        if flag:
            print('You didnot made any Transaction! \n')
    
    def take_loan(self, bank, amount):
        if self.loan_limit == 0:
            print('You alredy cross your loan limit!\n')
        else:
            amt = bank.loan_request(amount)
            if amt[0]:
                self.balance+=amount
                self.loan_limit-=1
                self.transaction_history.append(f'You toke total loan ${amount} current balance is ${self.balance}\n')
                print(amt[1])
            else:
                print(amt[1])
    def transfer_ammount(self, bank, AcNum, amount):
        if amount > self.balance:
            print('Insufficient Balance\n')
            return
        flag = True
        for i in range(0, len(bank.accounts)):
            if bank.accounts[i].account_number == AcNum:
                flag = False
                bank.accounts[i].balance+=amount
                self.balance-=amount
                self.transaction_history.append(f'Transfer total ${amount} to AcNum {AcNum} and current balance is ${self.balance}')
                print(f'Transfer total ${amount} to AcNum {AcNum} and current balance is ${self.balance}\n')
        if flag:
            print(f'Input account num {AcNum} is invalid')


bank = Bank()
acc1 = Account('1', '1','1','1')
acc2 = Account('2', '2','2','2')
bank.creat_an_account(acc1)
bank.creat_an_account(acc2)
acc_list=[acc1, acc2]

currAdmin = None
curUser = None
while True:
    if currAdmin==None and curUser==None:
        log = input('Admin or User login..? ')
        if log.lower() == 'admin':
            password = ''
            while password !='admin':
                password = input('Enter Admin Password(admin) :')
            currAdmin=bank
        elif log.lower() == 'user':
            if curUser == None:
                name = input('Enter you name :')
                for nm in acc_list:
                    if name == nm.name:
                        curUser = nm
                        break
                if curUser == None:
                    print('Account could not found! Plaese try with correct Name')
    elif currAdmin !=None and currAdmin.name == 'admin':
        print('\n')
        print('1 - Create An Account')
        print('2 - Delete An Account')
        print('3 - Check all Account & Users')
        print('4 - Check Total Balance')
        print('5 - Check Total Loan Amount')
        print('6 - Enable or Disable Loan Feature')
        print('7 - Logout!')

        cmd = int(input('\nEnter your choice: '))

        if cmd ==1:
            name = input('\nEnter your Full Name: ')
            email = input('\nEnter your Email: ')
            address = input('\nEnter your address: ')
            actype = input('\nEnter your Account Type(Saveings or Current): ')
            acc = Account(name, email, address, actype)
            currAdmin.creat_an_account(acc)
            acc_list.append(acc)
        elif cmd ==2:
            accNum = input('\nEnter your deleted account number: ')
            currAdmin.deleted_an_account(accNum)
        elif cmd ==3:
            currAdmin.check_all_account()
        elif cmd ==4:
            currAdmin.check_total_bank_balance()
        elif cmd ==5:
            currAdmin.check_total_loan()
        elif cmd==6:
            op = bool(input('Enable or Disable(True/False): '))
            if op:
                currAdmin.loan_feature(False)
            else:
                currAdmin.loan_feature(True)
        elif cmd==7:
            currAdmin = None
        else:
            cmd = int(input('Wrong Input : Enter any number 1-7: '))

    else:
        print('1 - Diposit in Account')
        print('2 - Withdraw in Account')
        print('3 - Check available balance')
        print('4 - Check Transaction History')
        print('5 - Take Loan from Bank')
        print('6 - Transfer Ammount')
        print('7 - Logout!')

        cmd = int(input('\nEnter your choice: '))
        if cmd ==1:
            amount = int(input('\nEnter your diposit amount: '))
            curUser.diposit(bank,amount)
        elif cmd ==2:
            amount = int(input('\nEnter your Withdrawal amount: '))
            curUser.withdraw(bank, amount)
        elif cmd ==3:
            curUser.check_available_balance()
        elif cmd ==4:
            curUser.check_transaction_history()
        elif cmd ==5:
            amount = int(input('\nEnter your Loan amount: '))
            curUser.take_loan(bank, amount)
        elif cmd==6:
            acNo = int(input('\nEnter your account number: '))
            amount = int(input('\nEnter transfer amount: '))
            curUser.transfer_ammount(bank, acNo, amount)
        elif cmd==7:
            currAdmin = None
            break
        else:
            cmd = int(input('Wrong Input : Enter any number 1-7: '))
