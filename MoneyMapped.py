## Author: u3272385 (University of Canberra)
## Date created: 20 April 2024
## Date Last Modified: 26 April 2024
#The inputs will be Month, Amount (Income/Expense), Description (Source/Cause of Income/Expense).
#The output will be Current Balance of a month, Income history of a month, Expense history of a month, and a Monthly Expense Analyser.

import tkinter as tk
from tkinter import ttk


def main(): #defining main function
    Finance_Tracker=MoneyMapped()

#Menu
    while True:
        print("____Money Mapped____\n"
                    "_______Menu_______:\n"
                    "0. To select Month\n"
                    "1. To Add Income\n"
                    "2. To Add Expense \n"
                    "3. To View Balance\n"
                    "4. To View Income History\n"
                    "5. To View Expense History\n"
                    "6. To View CashFlow\n"
                    "Press E to exit\n")
        user_input=input("Enter your option:")

#getting input        
        if user_input=="0":
            input_month=input("Enter Month:").upper()
            month_list=["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
            if input_month in month_list:
                Finance_Tracker.set_month(input_month)
                print(f"{input_month} is selected.")
            else:
                print("Month not correct!")
                continue

        elif user_input=="1":
            amount=float(input("Enter income amount:"))
            source = input("Enter Income Source:")
            print(Finance_Tracker.add_income(amount, source))
        elif user_input=="2":
            amount=float(input("Enter expense amount: "))
            cause = input("Enter the cause of expense:")
            print(Finance_Tracker.add_expense(amount, cause))
        elif user_input=="3":
            print(Finance_Tracker.view_balance())
        elif user_input=="4":
            print(Finance_Tracker.view_income())
        elif user_input=="5":
            print(Finance_Tracker.view_expense())
        elif user_input=="6":
            print(Finance_Tracker.view_cash_flow())
        elif user_input.lower() == "e":
            print("Thank You")
            break
        else:
            print("Invalid!!!")
       

class MoneyMapped:
    def __init__(self):
        self.month=None
        self.income={}
        self.expense={}
        self.balance=0

    def set_month(self,month):
        self.month = month
        self.balance=0.0
        self.expense[month]=[]
        self.income[month]=[]

        if month not in self.income:
            self.income[month]=[]
        if month not in self.expense:
            self.expense[month]=[]

    def add_income(self, amount, source):
        if not self.month:
            return "Select a month!"
        self.balance=self.balance + amount
        self.income[self.month].append({"amount":amount, "source": source})
        return f"${amount} added to Income for {self.month}. \nNew Balance: ${self.balance}"
    
    def add_expense(self, amount, cause):
        if not self.month:
            return "Select a month!"
        if amount>self.balance:
            return "No Sufficient Balance"
        self.balance=self.balance - amount
        self.expense[self.month].append({"amount":amount, "cause": cause})
        return f"${amount} added to expense for {self.month}. \nNew Balance: ${self.balance}"
    
    def view_balance(self):
        if not self.month:
            return "Select a month!"
        return f"Current balance: ${self.balance}"
    
    def view_income(self):
        monthly_income="\n".join([f"${income['amount']} :- {income['source']}" for income in self.income[self.month]])
        return f"{self.month}'s income history:\n" + monthly_income
    
    def view_expense(self):
        total_expenses=self.total_expense()
        expense_percentage=self.percentage()

        monthly_expense="\n".join([f"${expense['amount']} :- {expense['cause']}" for expense in self.expense[self.month]])

        monthly_analysis = "\nMonthly Expense Analysis \n"
        for cateogry, expense_percentage in self.percentage().items():
            monthly_analysis = monthly_analysis+ f"{cateogry}:{expense_percentage:.2f}% \n"
        return f"{self.month}'s expense history:\n" + monthly_expense + "\n" +monthly_analysis
    
    def view_cash_flow(self):
        return f"{self.view_balance()}\n Income Summary\n {self.view_income()}\n Expense Summary\n {self.view_expense()}"
    
    def total_expense(self):
        sum_of_expenses=sum(item['amount'] for item in self.expense[self.month])
        return sum_of_expenses
    
    def percentage(self):
        sum_of_expenses=self.total_expense()
        expense_items=self.expense[self.month]
        categories={}

        for item in expense_items:
            category=item['cause'].split()[0].capitalize()
            if category in categories:
                categories[category] += item['amount']
            else:
                categories[category] = item['amount']
        percentages= {category: ((amount/sum_of_expenses)*100) for category, amount in categories.items()}
        return percentages


if __name__ == "__main__":
    main()        



