class Atm:

    def __init__(self,cn,pn):

        self.cn=input("Enter Card Number: ")

        self.pn=input("Enter Pin Number: ")

      
    def CashWithdrawl(self):

        print("Whitdrawn $1000")

    def BalanceEnquiry(self):

        print("Remaing Balance:$16800")

atm1=Atm("","")

print(atm1.cn,atm1.pn)

atm1.CashWithdrawl()
atm1.BalanceEnquiry()