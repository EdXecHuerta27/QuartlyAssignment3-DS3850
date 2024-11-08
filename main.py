import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Connect to the database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Function to retrieve questions based on selected category
def get_questions(category):
    cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM {category}")
    return cursor.fetchall()

# Function to start the quiz
def start_quiz():
    selected_category = category_var.get()
    if not selected_category:
        messagebox.showerror("Error", "Please select a category")
        return
    
    # Fetch questions for the selected category
    global questions
    questions = get_questions(selected_category)
    
    if not questions:
        messagebox.showerror("Error", "No questions found in the selected category.")
        return
    
    # Close category window and open quiz window
    category_window.destroy()
    show_quiz_window()

# Function to show the quiz window
def show_quiz_window():
    global quiz_window, current_question_index, score
    quiz_window = tk.Tk()
    quiz_window.title("Quiz Bowl")
    quiz_window.geometry("400x300")
    
    current_question_index = 0
    score = 0
    
    # Display the first question
    display_question()
    
    quiz_window.mainloop()

# Function to display each question
def display_question():
    global current_question_index
    if current_question_index < len(questions):
        question_data = questions[current_question_index]
        
        # Clear previous question
        for widget in quiz_window.winfo_children():
            widget.destroy()
        
        # Display question text
        question_label = tk.Label(quiz_window, text=f"Q{current_question_index + 1}: {question_data[0]}", wraplength=350)
        question_label.pack(pady=10)
        
        # Display answer options with no pre-selection
        options = question_data[1:5]
        global selected_option
        selected_option = tk.StringVar(value="")  # Set initial value to empty to deselect all options
        
        for i, option in enumerate(options):
            tk.Radiobutton(quiz_window, text=option, variable=selected_option, value=chr(65 + i)).pack(anchor="w", padx=20)
        
        # Next button
        next_button = tk.Button(quiz_window, text="Next", command=check_answer)
        next_button.pack(pady=10)
    else:
        # Show the final score when quiz is over
        show_score()

# Function to check the answer and move to the next question
def check_answer():
    global current_question_index, score
    correct_answer = questions[current_question_index][5]  # The correct answer from the database
    if selected_option.get() == correct_answer:
        score += 1
    current_question_index += 1
    display_question()

# Function to display the final score
def show_score():
    for widget in quiz_window.winfo_children():
        widget.destroy()
    score_label = tk.Label(quiz_window, text=f"Your Score: {score}/{len(questions)}")
    score_label.pack(pady=20)
    close_button = tk.Button(quiz_window, text="Close", command=quiz_window.destroy)
    close_button.pack()

# Main Category Selection Window
category_window = tk.Tk()
category_window.title("Select Category")
category_window.geometry("300x200")

# Label and dropdown for category selection
tk.Label(category_window, text="Select a category:").pack(pady=10)
category_var = tk.StringVar()
categories = ["Python", "Finance", "Marketing", "Accounting", "Economics"]  # Adjust these based on actual table names
category_menu = ttk.Combobox(category_window, textvariable=category_var, values=categories)
category_menu.pack(pady=10)

# Start Quiz button
start_button = tk.Button(category_window, text="Start Quiz Now", command=start_quiz)
start_button.pack(pady=20)

category_window.mainloop()
