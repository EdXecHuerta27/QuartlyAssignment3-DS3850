import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create the "Accounting101" table for storing accounting questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS Accounting101 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Function to insert a question into the "Accounting101" table
def insert_accounting_question(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO Accounting101 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Sample accounting-related questions data
accounting_questions = [
    ("What is the primary purpose of financial accounting?", 
     "To provide information for internal decision-making", 
     "To record every business transaction", 
     "To provide financial information to external users", 
     "To prepare the budget", "C"),
    
    ("Which of the following is classified as an asset?", 
     "Accounts Payable", "Inventory", "Owner's Equity", "Revenue", "B"),
    
    ("What does the term 'liabilities' refer to in accounting?", 
     "A company's resources", 
     "Obligations a company owes to others", 
     "A company’s revenue streams", 
     "A company’s expenses", "B"),
    
    ("Which financial statement provides information about a company's financial position at a specific date?", 
     "Income Statement", "Cash Flow Statement", "Balance Sheet", "Statement of Owner’s Equity", "C"),
    
    ("What is the accounting equation?", 
     "Assets = Liabilities + Revenue", 
     "Assets = Liabilities + Expenses", 
     "Assets = Liabilities + Equity", 
     "Assets = Liabilities - Equity", "C"),
    
    ("Which type of account has a normal debit balance?", 
     "Liabilities", "Revenues", "Expenses", "Owner’s Equity", "C"),
    
    ("What is depreciation?", 
     "An increase in asset value", 
     "A decrease in asset value due to wear and tear", 
     "An expense that increases equity", 
     "The amount owed on a loan", "B"),
    
    ("Which principle states that expenses should be recorded when incurred?", 
     "Revenue Recognition Principle", "Matching Principle", 
     "Cost Principle", "Economic Entity Principle", "B"),
    
    ("What is the purpose of an income statement?", 
     "To show a company’s profitability over a period of time", 
     "To show the company’s assets and liabilities", 
     "To display cash inflows and outflows", 
     "To summarize owner's equity", "A"),
    
    ("What does 'double-entry accounting' refer to?", 
     "Recording each transaction in two different accounts", 
     "Recording both debits and credits for each transaction", 
     "Using two different accounting periods", 
     "Recording both revenues and expenses in one statement", "B")
]

# Insert sample accounting questions into the "Accounting101" table
for question in accounting_questions:
    insert_accounting_question(*question)

print("Accounting questions inserted successfully into the Accounting101 table.")

# Close the connection
conn.close()
