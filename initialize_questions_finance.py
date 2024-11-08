import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create the "Finance101" table for storing finance questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS Finance101 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Function to insert a question into the "Finance101" table
def insert_finance_question(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO Finance101 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Sample finance-related questions data
finance_questions = [
    ("What is the primary goal of financial management?", 
     "Minimizing costs", "Maximizing revenue", "Maximizing shareholder wealth", "Ensuring liquidity", "C"),
    
    ("Which of the following is an example of a current asset?", 
     "Inventory", "Building", "Equipment", "Patent", "A"),
    
    ("What does the term 'liquidity' refer to in finance?", 
     "The ability to pay off long-term debt", "The ability to convert assets to cash quickly", 
     "The profitability of a company", "The amount of debt in a company", "B"),
    
    ("Which financial statement shows a company's revenue and expenses?", 
     "Balance Sheet", "Income Statement", "Cash Flow Statement", "Statement of Equity", "B"),
    
    ("What is the purpose of a budget in financial planning?", 
     "To measure past performance", "To forecast future profits", "To allocate resources", "To evaluate staff performance", "C"),
    
    ("Which of the following ratios is used to assess a company’s profitability?", 
     "Debt-to-equity ratio", "Current ratio", "Gross margin ratio", "Inventory turnover ratio", "C"),
    
    ("What is the formula for calculating the Net Present Value (NPV)?", 
     "PV - FV", "Sum of discounted cash flows - initial investment", "Total Revenue - Total Cost", "Profit - Expenses", "B"),
    
    ("Which type of finance focuses on securities and the management of financial institutions?", 
     "Corporate Finance", "Investment Banking", "Public Finance", "Personal Finance", "B"),
    
    ("What does the 'P/E ratio' stand for?", 
     "Price to Earnings ratio", "Profit to Equity ratio", "Profit to Expense ratio", "Present Earnings ratio", "A"),
    
    ("What is the purpose of diversification in an investment portfolio?", 
     "To maximize short-term profits", "To minimize risk by spreading investments", 
     "To guarantee high returns", "To increase liquidity", "B")
]

# Insert sample finance questions into the "Finance101" table
for question in finance_questions:
    insert_finance_question(*question)

print("Finance questions inserted successfully into the Finance101 table.")

# Close the connection
conn.close()
