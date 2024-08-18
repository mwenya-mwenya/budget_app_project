import unittest
import main as budget
from importlib import reload

reload(budget)

class UnitTests(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.food = budget.Category("Food")
        self.entertainment = budget.Category("Entertainment")
        self.business = budget.Category("Business")

    def tearDown(self):
        
        self.food = budget.Category("Food")
        self.entertainment = budget.Category("Entertainment")
        self.business = budget.Category("Business")

    def test_create_spend_chart(self):
        self.food.deposit(900, "deposit")
        self.entertainment.deposit(900, "deposit")
        self.business.deposit(900, "deposit")
        self.food.withdraw(105.55)
        self.entertainment.withdraw(33.40)
        self.business.withdraw(10.99)
        actual = budget.create_spend_chart([self.business, self.food, self.entertainment])
        expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
        self.assertEqual(actual, expected, 'Expected different chart representation. Check that all spacing is exact.')
    
    def test_deposit(self):
        self.food.deposit(30,"deposit")
        actual = self.food.ledger[0]
        expected = {'amount': 30, 'description': 'deposit'}
        self.assertEqual(actual,expected,'Expected different chart representation. check deposit is appending entries correctly')

    def test_withdraw(self):
        self.food.deposit(600,"deposit")
        self.food.withdraw(360,'cavier')
        actual = self.food.ledger[1]
        expected = {'amount': -360, 'description': 'cavier'}
        self.assertEqual(actual,expected,'Expected different chart representation. check deposit is appending entries correctly')

    def test_transfer(self):
        self.food.deposit(600,"deposit")
        self.food.transfer(360,self.entertainment)
        actual_1 = self.food.ledger[1]
        expected_1 = {'amount': -360, 'description': 'Transfer to Entertainment'}
        self.assertEqual(actual_1,expected_1,'Expected different chart representation. check deposit is appending entries correctly')
        actual_2 = self.entertainment.ledger[0]
        expected_2 = {'amount': 360, 'description': 'Transfer from Food'}
        self.assertEqual(actual_2,expected_2,'Expected different chart representation. check deposit is appending entries correctly')
    
    def test_balance(self):
        self.food.deposit(600,"deposit")
        self.food.withdraw(500,"all bar one")
        actual = self.food.balance
        expected = 100
        self.assertEqual(actual,expected,'Review check_fund ensire return is self.balance >= amount provided ')
    
    
    def test_check_funds(self):
        self.food.deposit(600,"deposit")
        actual = self.food.check_funds(600)
        expected = True
        self.assertTrue(actual,'Review check_fund ensire return is self.balance >= amount provided ')
    

if __name__ == '__main__':
    unittest.main()
