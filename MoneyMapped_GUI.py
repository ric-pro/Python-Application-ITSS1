## Author: u3272385 (University of Canberra)
## Date created: 20 April 2024
## Date Last Modified: 26 April 2024
#The inputs will be Month, Amount (Income/Expense), Description (Source/Cause of Income/Expense).
#The output will be Current Balance of a month, Income history of a month, Expense history of a month, and a Monthly Expense Analyser.




import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class gui_MoneyMapped: #Graphical User Interface 
    def __init__(self,root):
        self.root=root
        self.root.title("MoneyMapped")
        self.tracker=MoneyMapped()

#Defining a heading
        self.header_name = ttk.Label(root, text="MoneyMapped", font=("Arial", 40, "bold"), foreground="#2F3C7E", background="#FBEAEB")
        self.header_name.grid(row=0, columnspan=4, padx=10, pady=10)

#Selecting month from drop down menu
        self.month_gui=ttk.Label(root, text="Select Month:")
        self.month_gui.grid(row=1, column=0,padx=10,pady=10)
        self.month_gui_list=["January", "Febraury", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.month_gui_variable=tk.StringVar()
        self.month_gui_dropdown=ttk.Combobox(root, textvariable=self.month_gui_variable, values=self.month_gui_list)
        self.month_gui_dropdown.grid(row=1, column=1, padx=10, pady=10)
        self.month_gui_dropdown.bind("<<ComboboxSelected>>", self.set_month)

 #displaying selected month       
        self.set_month_lavel=ttk.Label(root, text="Selected Month: None")
        self.set_month_lavel.grid(row=1, column=2, padx=10, pady=10)

#Area to input amount 
        self.amount_gui=ttk.Label(root, text="Amount:")
        self.amount_gui.grid(row=2, column=0, padx=10, pady=10)
        self.amount_input=ttk.Entry(root)
        self.amount_input.insert(0, "Enter amount here")
        self.amount_input.grid(row=2, column=1, padx=10, pady=10)
        self.amount_input.bind("<FocusIn>", lambda event: self.clear_desc(event, self.amount_input))
        self.amount_input.bind("<FocusOut>", lambda event: self.renter_desc(event, self.amount_input))

#Area to input description
        self.explanation_gui=ttk.Label(root, text="Description:")
        self.explanation_gui.grid(row=3, column=0, padx=10, pady=10)
        self.explanation_input=ttk.Entry(root)  
        self.explanation_input.insert(0, "Enter description here")
        self.explanation_input.grid(row=3, column=1, padx=10, pady=10)
        self.explanation_input.bind("<FocusIn>", lambda event: self.clear_desc(event, self.explanation_input))
        self.explanation_input.bind("<FocusOut>", lambda event: self.renter_desc(event, self.explanation_input))

#Button to add amount to income
        self.add_income_initiate=ttk.Button(root, text="Add Amount to Income", command=self.add_income, style='AddIncome.TButton')
        self.add_income_initiate.grid(row=4, column=1, padx=10, pady=10)
        self.style = ttk.Style()
        self.style.configure('AddIncome.TButton', background='blue')

#Button to add amount to expense
        self.add_expense_initiate=ttk.Button(root, text="Add Amount to Expense", command=self.add_expense, style='AddExpense.TButton')
        self.add_expense_initiate.grid(row=4, column=2, padx=10, pady=10)
        self.style = ttk.Style()
        self.style.configure('AddExpense.TButton', background='Red')

#Button to view balance
        self.view_balance_initiate=ttk.Button(root, text="Click to View Balance", command=self.view_balance)
        self.view_balance_initiate.grid(row=5, column=0, padx=10, pady=10)

#Button to view income history
        self.view_IncomeHistory_initiate=ttk.Button(root, text="Click for Income History", command=self.income_history)
        self.view_IncomeHistory_initiate.grid(row=5, column=1, padx=10, pady=10)

#Button to view expense history
        self.view_ExpenseHistory_initiate=ttk.Button(root, text="Click for Expense History & Expense Analysis", command=self.expense_history)
        self.view_ExpenseHistory_initiate.grid(row=5, column=2, padx=10, pady=10)

#Button to view cash flow
        self.view_CashFlow_initiate=ttk.Button(root, text="Click to View Cash Flow", command=self.cash_flow)
        self.view_CashFlow_initiate.grid(row=5, column=3, padx=10, pady=10)

        self.load_data_label = tk.Label(root, text="Click the button to load txt file named 'test_data1' or 'test_data2' in the zip file to test the functionality -->", bg="lightgreen")
        self.load_data_label.grid(row=6, column=1, padx=10, pady=10, columnspan=2, sticky="w")

#Button to load data from file
        self.load_gui_initiate=tk.Button(root, text="Load Data from file",bg='lightblue', command=self.load_data)
        self.load_gui_initiate.grid(row=6, column=3, padx=10, pady=10)

#Button to quit the program        
        exit_button=tk.Button(root, text="Quit",bg='red', command=quit, width=16)
        exit_button.grid(row=7, column= 3, padx=10, pady=10)

#Area to display output
        self.output_display=tk.Text(root, height=15, width=100)
        self.output_display.grid(row=11, columnspan=4, padx=10, pady=10)

#Box which consist of informations on how to use the application   
        self.instruction = tk.Text(root, height=8, width=100, wrap=tk.WORD, background="#FBEAEB")
        self.instruction.insert(tk.END, "How to use the Application\n")
        self.instruction.tag_configure("bold", font=("Arial", 15, "bold"))
        self.instruction.tag_add("bold", "1.0", "1.end")
        self.instruction.insert(tk.END, "1. Choose a month from dropdown menu.\n")
        self.instruction.insert(tk.END, "2. Input income/expense(in numbers) and description(source/casue of income/expense) using the respective buttons.\n")
        self.instruction.insert(tk.END, "3. Click 'Add Amount to Income' button to add the amount to incomes of the selected month. \n")
        self.instruction.insert(tk.END, "4. Click 'Add Amount to Expense' button to add the amount to expenses of the selected month. \n")
        self.instruction.insert(tk.END, "5. Choose from the buttons 'View Balance', 'Income History', 'Expense History', 'Cash Flow' to perform the respective calculations. \n")
        self.instruction.insert(tk.END, "6. In order to load data from external file, click 'Load data from file' and choose the 'txt' file that contains the data.\n")
        self.instruction.insert(tk.END, "7. After loading the data, choose the desired option. For eg, clicking 'View Balance' button will show balance amount after calculating from data's in the 'txt' files\n")
        self.instruction.grid(row=12, columnspan=6, padx=10, pady=10)
        self.instruction.config(state=tk.DISABLED)

        
   

    
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
        return f"{self.view_balance()}\n\n {self.view_income()}\n\n {self.view_expense()}"
    
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
    
    def data_from_file(self,data):
        self.income=data.get('income', {})
        self.expense=data.get('expense', {})
        self.month=data.get('month', None)
        self.update_balance()

    def load_data(self, name):
        with open(name, 'r') as file:
            data=eval(file.read())
            self.data_from_file(data)
        return True   
    
    def update_balance(self):
        total_income = sum(item['amount'] for item in self.income[self.month])
        total_expense = sum(item['amount'] for item in self.expense[self.month])
        self.balance = total_income - total_expense 
        


if __name__ == "__main__":
    root=tk.Tk()
    app=gui_MoneyMapped(root)
    root.mainloop()