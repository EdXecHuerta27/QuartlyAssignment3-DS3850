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
    
    global questions
    questions = get_questions(selected_category)
    
    if not questions:
        messagebox.showerror("Error", "No questions found in the selected category.")
        return
    
    category_window.destroy()
    show_quiz_window()

# Function to show the quiz window
def show_quiz_window():
    global quiz_window, current_question_index, score
    quiz_window = tk.Tk()
    quiz_window.title("Quiz Bowl")
    quiz_window.geometry("500x400")
    quiz_window.configure(bg="#f0f8ff")  # Light blue background
    
    current_question_index = 0
    score = 0
    
    display_question()
    
    quiz_window.mainloop()

# Function to display each question
def display_question():
    global current_question_index
    if current_question_index < len(questions):
        question_data = questions[current_question_index]
        
        for widget in quiz_window.winfo_children():
            widget.destroy()
        
        # Frame for question
        question_frame = tk.Frame(quiz_window, bg="#d1e7f5", bd=2, relief="solid")
        question_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Display question text with larger font
        question_label = tk.Label(
            question_frame, text=f"Q{current_question_index + 1}: {question_data[0]}", 
            wraplength=450, font=("Arial", 14, "bold"), bg="#d1e7f5"
        )
        question_label.pack(pady=10, padx=10)
        
        options = question_data[1:5]
        global selected_option
        selected_option = tk.StringVar(value="")  # Ensure no pre-selection
        
        # Frame for options
        options_frame = tk.Frame(question_frame, bg="#f5faff")
        options_frame.pack(pady=10)
        
        for i, option in enumerate(options):
            tk.Radiobutton(
                options_frame, text=option, variable=selected_option, 
                value=chr(65 + i), font=("Arial", 12), bg="#f5faff", 
                activebackground="#e0f2fe", highlightbackground="#cccccc", anchor="w"
            ).pack(fill="x", padx=15, pady=5)
        
        # Next button with color and padding
        next_button = tk.Button(
            quiz_window, text="Next", command=check_answer, font=("Arial", 12, "bold"), 
            bg="#4caf50", fg="white", activebackground="#66bb6a", padx=20, pady=5
        )
        next_button.pack(pady=10)
    else:
        show_score()

# Function to check the answer and move to the next question
def check_answer():
    global current_question_index, score
    correct_answer = questions[current_question_index][5]
    if selected_option.get() == correct_answer:
        score += 1
    current_question_index += 1
    display_question()

# Function to display the final score
def show_score():
    for widget in quiz_window.winfo_children():
        widget.destroy()
    score_label = tk.Label(
        quiz_window, text=f"Your Score: {score}/{len(questions)}", 
        font=("Arial", 18, "bold"), bg="#f0f8ff"
    )
    score_label.pack(pady=20)
    close_button = tk.Button(
        quiz_window, text="Close", command=quiz_window.destroy, 
        font=("Arial", 12, "bold"), bg="#ff7043", fg="white", 
        activebackground="#ff8a65", padx=20, pady=5
    )
    close_button.pack(pady=10)

# Main Category Selection Window
category_window = tk.Tk()
category_window.title("Select Category")
category_window.geometry("350x250")
category_window.configure(bg="#f0f8ff")

# Category selection label and dropdown
tk.Label(
    category_window, text="Select a category:", font=("Arial", 14, "bold"), bg="#f0f8ff"
).pack(pady=15)
category_var = tk.StringVar()
categories = ["Python", "Finance", "Marketing", "Accounting", "Economics"]  # Adjust these based on table names
category_menu = ttk.Combobox(category_window, textvariable=category_var, values=categories, font=("Arial", 12))
category_menu.pack(pady=10)

# Start Quiz button
start_button = tk.Button(
    category_window, text="Start Quiz Now", command=start_quiz, 
    font=("Arial", 12, "bold"), bg="#4caf50", fg="white", 
    activebackground="#66bb6a", padx=20, pady=5
)
start_button.pack(pady=20)

category_window.mainloop()
