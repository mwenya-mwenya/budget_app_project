class Category:
    total_balance = 0 #total balance accross all accounts
     
    def __init__(self,category):        
        self.category = category
        self.ledger = []
        self.balance = 0
        Category.total_balance += self.balance

    def __str__(self):

        output = ''
        balance = f"{self.balance:.2f}"
        output +=f"{self.category.center(30,'*')}\n"
        
        for idx in range(len(self.ledger)):

            amount_str = f"{self.ledger[idx]['amount']:.2f}"
            space = 0
            desc_str = self.ledger[idx]['description']
            desc_str_length = len(desc_str)

            if desc_str_length <= 23:
                space = 29 - desc_str_length
            
            output += f"{desc_str[:23]} {amount_str[:7].rjust(space)}\n"
        output += f"Total: {balance[:7]}"
        return output

    def get_balance(self):
        return self.balance

    def deposit(self,amount,description=''):
        self.ledger.append({'amount':amount, 'description':description})
        self.balance += amount
        Category.total_balance += amount
    
    def check_funds(self,amount):
        return self.balance >= amount
    
    def withdraw(self,amount,description=''):      
        if self.check_funds(amount):
            self.balance -= amount
            Category.total_balance -= amount
            self.ledger.append({'amount':-amount, 'description':description})
            
            return True
        return False
    
    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.category}")
            other_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False 
       
def create_spend_chart(categories):

    total_expenditure =  abs(sum(entry['amount'] for cat in categories for entry in cat.ledger if entry['amount'] < 0))
    cats = {}

    for item in categories:      
        amount_2 = sum(a['amount'] for a in item.ledger if a['amount'] < 0)
        cats[item.category] = round(abs(amount_2)/total_expenditure,2)*10
   
    unsorted_cats = [a for a in cats]
    percs = [cats[b] for b in unsorted_cats]  
    max_cat = list(len(a) for a in unsorted_cats)    
    
    str_1 = 'Percentage spent by category\n'
   
    for i in range(11):
        if i > 0 and i < 10:
            str_1 += f" {(10 - i) * 10}|"
        elif i == 10:
            str_1 += f"  {(10 - i) * 10}|"
        else:        
            str_1 += f"{(10 - i) * 10}|"
        for idx,b in enumerate(percs):
            if b >= (10-i) and b != 0:
                if idx == len(percs)-1:
                    str_1 += ' o  '
                else:
                    str_1 += ' o '
            else:
                if idx == len(percs)-1:
                    str_1 += '    '
                else:    
                    str_1 += '   '
        if i == 10:
            dashes = (len(unsorted_cats)*3)+1
            
            str_1 += '\n'+'    '+('-'*dashes) 
            
        str_1 += '\n'
    
    for b in range(max(max_cat)):
        for idx,c in enumerate(max_cat):
            if idx == 0:
                str_1 += '   '
            if c <= b:
                str_1 += '   '                
                continue
                                        
            str_1 += "  "+unsorted_cats[idx][b]
            if idx == len(max_cat)-1:
                str_1 += '  '
        if b == max(max_cat)-1:
            break
        else:    
            str_1 += '\n'
                 
    return str_1 

 






    


