# QuartlyAssignment3-DS3850

Here’s a template for a README file that outlines your project, provides instructions, and describes the functionality. Feel free to adjust any details to suit your specific needs.

Quiz Bowl Project - GUI for Quiz Application
Project Overview
This project is a Quiz Bowl Application designed for users to take quizzes in various subjects via a user-friendly graphical user interface (GUI). The project is implemented in Python using tkinter for the front end and SQLite for the back-end database.

The GUI allows users with no coding knowledge to select a quiz category and answer questions. The back end stores questions in a database with five different tables, each corresponding to a separate subject.

Features
Category Selection: Users can choose from five quiz categories (Python, Finance, Marketing, Accounting, and Economics) in the initial window.
Question Display: Each question is shown one by one, with four answer options.
Answer Selection: Users can select their answer, with no answer pre-selected for any question.
Score Display: Once the quiz is completed, the user's score is displayed.
Requirements
Python 3.x
tkinter (usually included with Python)
SQLite (for managing the database)
Installation
Clone or download this repository to your local machine.
Ensure Python is installed on your machine.
(Optional) Set up a virtual environment:
bash
Copy code
python -m venv quiz_env
source quiz_env/bin/activate  # On Windows, use quiz_env\Scripts\activate
Install any additional dependencies if necessary (though tkinter and sqlite3 should be included with Python).
Database Setup
The back end contains a SQLite database file (questions.db) with five tables:

Python: Contains questions related to Python programming.
Finance: Contains finance-related questions.
Marketing: Contains marketing-related questions.
Accounting: Contains accounting-related questions.
Economics: Contains economics-related questions.
Each table has a minimum of 10 questions, each with four possible answers and one correct answer.

Usage
Run the Program: Start the program by running the main Python file:

bash
Copy code
python quiz_bowl_gui.py
Select a Category: The first window allows the user to select a quiz category. Choose a category and click “Start Quiz Now.”

Answer Questions: In the quiz window, each question appears one by one. Select an answer and click “Next” to proceed to the next question.

View Score: Once all questions are answered, the final score is displayed.

File Structure
quiz_bowl_gui.py: The main file that contains the GUI logic.
database_scripts: Folder containing scripts to manage the database (e.g., add, delete, or read questions).
README.md: Project overview and instructions (this file).
questions.db: SQLite database containing tables with questions.
Example Screenshots
(Optional: Add screenshots showing the category selection window, quiz questions, and final score screen.)


