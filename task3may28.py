import random

class people:
    def __init__(self):
        country_list = ['China', 'UK', 'USA', 'Saudi', 'Ukraine']
        fir_name_list = ['Eric', 'Alex', 'Massoud', 'Atahan']
        last_name_list = ['Wang', 'Zhang', 'Mohammed', 'Kayhan']
        self._first_name = fir_name_list[random.randint(0,len(fir_name_list)-1)]
        self._last_name = last_name_list[random.randint(0,len(last_name_list)-1)]
        self._country = country_list[random.randint(0,len(country_list)-1)]

class client(people):
    def __init__(self):
        people.__init__(self)
        self._balance = random.randint(0,1000000)
        # self._max_loan = 900000
        # self.debt = 0
        self.SelfIntro()

    def SelfIntro(self):
        print('-' * 25)
        print(f"My first name is {self._first_name}")
        print(f"My last name is {self._last_name}")
        print(f'I am from {self._country}')
        print('-' * 25)

    def BalanceReport(self):
        print(f'My current balance is {self._balance}')

class Bank:
    def __init__(self):
        print('This is Bank of Freddie Dragons')
        print('Welcome'.center(len('This is Bank of Freddie Dragons')))
        print('Our main Acitivity:  1. Giving loans to people\n \
                    2. Requirements: Have to be in the correct country & has to be poor.\n \
                    3. Size of a loan: Unlimited.')

    def CheckifPoor(self,p:client) -> bool:
        if p._balance < 500000:
            return True
        return False

    def CheckRightCountry(self,p:client) -> bool:
        right_countries = ['China', 'UK']
        if p._country in right_countries:
            return True
        return False
    
    def GiveLoan(self,p:client):
        print(f'You can get a loan, how much money you want to get?')
        try:
            money = int(input('Enter a valid number or enter \'0\' to stop loanning: '))
            while money:
                if money > 0:
                    p._balance += money
                    # p.debt += money
                    # p._max_loan -= money
                    p.BalanceReport()
                    money = int(input('Enter a valid number again or enter \'0\' to stop loanning: '))
                else:
                    money = int(input('This number is less than 0, please enter a valid number again: '))
        except:
            money = int(input('LAST WARNING! Enter a valid number or enter \'0\' to stop loanning: '))

    def FinalResult(self,p:client):
        res1 = self.CheckifPoor(p)
        res2 = self.CheckRightCountry(p)
        if res1:
            if res2:
                self.GiveLoan(p)
            else:
                print('You are in the wrong country, you can\'t get loan')
        else:
            if res2:
                print('You should get richer on you own')
            else:
                print('You are neither poor or from the right country, you need to get richer')


def main():
    c = client()
    bank = Bank()
    bank.FinalResult(c)


if __name__ == '__main__':
    main()