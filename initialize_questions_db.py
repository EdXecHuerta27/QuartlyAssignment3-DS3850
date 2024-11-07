import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create the "DS3850" table for storing questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS DS3850 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Function to insert a question into the "DS3850" table
def insert_question(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO DS3850 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Sample questions data
questions = [
    ("Which of the following is used to print text to the screen in Python?", "print()", "echo()", "display()", "text()", "A"),
    ("What is the output of the following code: print(5 + 3 * 2)?", "16", "11", "13", "10", "B"),
    ("Which of the following is a correct variable name in Python?", "1st_number", "firstNumber", "first number", "first-number", "B"),
    ("What data type does Python assign to 5.5 by default?", "Integer", "Float", "String", "Boolean", "B"),
    ("What will len('Hello') return?", "4", "5", "6", "Error", "B"),
    ("Which of the following keywords is used to define a function in Python?", "func", "define", "function", "def", "D"),
    ("What will the following code output? print('2' + '3')", "5", "23", "6", "Error", "B"),
    ("Which of the following is the correct syntax for a for loop?", "for (i in range 5):", "for i in range(5)", "for i in range(5):", "for i = 1 to 5:", "C"),
    ("How can you insert a comment in Python code?", "// This is a comment", "# This is a comment", "/* This is a comment */", "** This is a comment **", "B"),
    ("Which operator is used to check if two values are not equal?", "=", "==", "!=", "<>", "C"),
]

# Insert sample questions into the "DS3850" table
for q in questions:
    insert_question(*q)

print("Questions inserted successfully into the DS3850 table.")

# Close the connection
conn.close()
