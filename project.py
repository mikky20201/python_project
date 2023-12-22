from uuid import uuid4
from datetime import datetime



class Expense:
    def __init__(self, title, amount):
        """
        This method initializes the attributes
        """
        self.id = str(uuid4())
        self.title = str(title)
        self.amount = float(amount)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, title = None, amount = None):
        """
        This method allows updating the title and/or amount of the expense
        """
        self.title = title
        self.amount = amount
        self.updated_at = datetime.utcnow()
        return f"title: {self.title}, amount: {self.amount} has been updated"
    
    
    def to_dict(self):
        """
        This method returns a dictionary representation of the expense
        """
        expense_dict = {'id': self.id, 'title': self.title, 'amount': self.amount, 'created_at': str(self.created_at), 'updated_at': str(self.updated_at)}
        return expense_dict

    def __str__(self) -> str:
        return f"{self.id}_{self.title}_{self.amount}_{self.created_at}_{self.updated_at}"
    

class ExpenseDatabase:
    def __init__(self):
        """
        This method initializes the expenses list
        """
        self.expenses = []

    def add_expense(self, expense):
        """
        This method adds an expense to the database
        """
        self.expenses.append(expense.to_dict())
        print('expense added successfully!')

    def remove_expense(self, expense_id):
        """
        This method removes an expense from the database
        """
        self.expenses = [item_expense for item_expense in self.expenses if item_expense['id'] != expense_id]
        print(f"{expense_id} successfully removed!")

    def get_expense_by_id(self, expense_id):
        """
        This method get an expense by ID
        """
        for item_expense in self.expenses:
            if item_expense['id'] == expense_id:
                return item_expense
                break
        
    def get_expense_by_title(self, expense_title):
        """
        This method get expenses by title and returns a list
        """
        return [item_expense for item_expense in self.expenses if item_expense['title'] == expense_title]
         
    def to_dict(self): 
        """
        This method returns a list of dictionaries representing each expense in the database
        """
        return self.expenses

expense_1 = Expense(title = 'Out_of_pocket', amount = 2000)
expense_2 = Expense(title = 'Fuel', amount = 5000.50)
expense_db = ExpenseDatabase()

# expense_1 = Expense(title = 'Out_of_pocket', amount = 2000)
# expense_2 = Expense(title = 'Fuel', amount = 5000.50)
# expense_3 = Expense(title = 'Fuel', amount = 7000.50)
# print(expense_1.update(title='Out_of_pocket', amount= 3000))

# print(expense_1.to_dict())
# print(expense_2.to_dict())
# print(expense_3.to_dict())

# expense_db.add_expense(expense_1)
# expense_db.add_expense(expense_2)
# print(expense_db.expenses)  


