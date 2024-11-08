import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create the "Economics101" table for storing economics questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS Economics101 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Function to insert a question into the "Economics101" table
def insert_economics_question(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO Economics101 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Sample economics-related questions data
economics_questions = [
    ("What is the basic economic problem?", 
     "Unlimited resources and limited wants", 
     "Unlimited wants and limited resources", 
     "Equal distribution of wealth", 
     "Perfect competition in markets", "B"),
    
    ("Which of the following defines 'opportunity cost'?", 
     "The cost of producing one more unit of a good", 
     "The value of the next best alternative foregone", 
     "The cost of all inputs used in production", 
     "The difference between total revenue and total cost", "B"),
    
    ("What is the law of demand?", 
     "Price and quantity demanded are inversely related", 
     "Price and quantity demanded are directly related", 
     "Demand is independent of price", 
     "Demand increases as supply increases", "A"),
    
    ("Which type of market structure is characterized by a single seller?", 
     "Monopoly", "Oligopoly", "Perfect competition", "Monopolistic competition", "A"),
    
    ("What is 'inflation'?", 
     "A decrease in the overall price level", 
     "An increase in the overall price level", 
     "An increase in economic output", 
     "A decrease in unemployment", "B"),
    
    ("Which of the following is a macroeconomic goal?", 
     "Maximizing individual wealth", "Achieving full employment", 
     "Maximizing corporate profits", "Increasing individual consumer choice", "B"),
    
    ("What is Gross Domestic Product (GDP)?", 
     "The total output produced by a country in one year", 
     "The total money supply in the economy", 
     "The total amount of goods and services imported", 
     "The total stock of goods held by retailers", "A"),
    
    ("Which economic theory focuses on supply-side policies to stimulate growth?", 
     "Keynesian economics", "Classical economics", 
     "Monetary policy", "Supply-side economics", "D"),
    
    ("What does a 'trade deficit' imply?", 
     "A country exports more than it imports", 
     "A country imports more than it exports", 
     "The government spends more than it earns", 
     "The value of exports equals imports", "B"),
    
    ("What is the role of central banks in an economy?", 
     "To increase taxes", 
     "To manage the nation's money supply and interest rates", 
     "To control all prices", 
     "To allocate resources", "B")
]

# Insert sample economics questions into the "Economics101" table
for question in economics_questions:
    insert_economics_question(*question)

print("Economics questions inserted successfully into the Economics101 table.")

# Close the connection
conn.close()
