import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create the "Marketing101" table for storing marketing questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS Marketing101 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Function to insert a question into the "Marketing101" table
def insert_marketing_question(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO Marketing101 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Sample marketing-related questions data
marketing_questions = [
    ("What is the main purpose of marketing?", 
     "To increase market share", "To satisfy customer needs", "To promote a product", "To create advertisements", "B"),
    
    ("Which of the following is part of the marketing mix?", 
     "Price", "Position", "Promotion", "People", "A"),
    
    ("What is market segmentation?", 
     "Dividing a market based on geographical areas", "Dividing a market into distinct groups of buyers", 
     "Offering different products for different markets", "Creating brand loyalty", "B"),
    
    ("What does the term 'brand equity' refer to?", 
     "The value added to a product by its brand name", "The quality of a product", 
     "The cost of marketing", "The profitability of a brand", "A"),
    
    ("Which of the following is an example of primary data in marketing research?", 
     "Published articles", "Surveys conducted by the company", "Government reports", "Industry publications", "B"),
    
    ("What is the '4Ps' model in marketing?", 
     "Product, Promotion, Price, Place", "People, Process, Profit, Product", 
     "Price, Place, Product, Profit", "Promotion, Product, Place, People", "A"),
    
    ("Which strategy focuses on retaining existing customers?", 
     "Customer acquisition", "Customer retention", "Product diversification", "Market segmentation", "B"),
    
    ("What is a target market?", 
     "A group of customers with similar needs", "The price of a product", 
     "The physical location of a store", "The sales target for the quarter", "A"),
    
    ("What is a common goal of digital marketing?", 
     "Increasing physical store visits", "Reducing the cost of product development", 
     "Enhancing online presence", "Improving customer service at stores", "C"),
    
    ("Which of the following is a characteristic of a niche market?", 
     "Broad and diverse audience", "High competition", "Specialized products and services", "Low customer loyalty", "C")
]

# Insert sample marketing questions into the "Marketing101" table
for question in marketing_questions:
    insert_marketing_question(*question)

print("Marketing questions inserted successfully into the Marketing101 table.")

# Close the connection
conn.close()
