import tkinter as tk
from tkinter import messagebox

# Dictionary to store South African questions, options, and correct answer
quiz_data = {
    "Who was the first black president of South Africa?": {
        "options": ["Nelson Mandela", "Jacob Zuma", "Thabo Mbeki", "FW de Klerk"],
        "correct": "Nelson Mandela"
    },
    "Which city is known as the 'Mother City' of South Africa?": {
        "options": ["Durban", "Pretoria", "Johannesburg", "Cape Town"],
        "correct": "Cape Town"
    },
    "What is the national flower of South Africa?": {
        "options": ["Protea", "Rose", "Sunflower", "Lily"],
        "correct": "Protea"
    },
    "Which South African athlete won the 800m gold medal at the 2012 Olympics?": {
        "options": ["Caster Semenya", "Wayde van Niekerk", "Oscar Pistorius", "Chad le Clos"],
        "correct": "Caster Semenya"
    },
    "What is the capital city of South Africa?": {
        "options": ["Pretoria", "Cape Town", "Bloemfontein", "Johannesburg"],
        "correct": "Pretoria"
    },
    "What is the name of South Africa's national rugby team?": {
        "options": ["The Springboks", "The Proteas", "The Sharks", "The Stormers"],
        "correct": "The Springboks"
    },
    "Which famous South African leader wrote the autobiography 'Long Walk to Freedom'?": {
        "options": ["Desmond Tutu", "Steve Biko", "Nelson Mandela", "Jacob Zuma"],
        "correct": "Nelson Mandela"
    },
    "Which South African city is known as the 'City of Gold'?": {
        "options": ["Johannesburg", "Durban", "Pretoria", "Port Elizabeth"],
        "correct": "Johannesburg"
    },
    "Which South African group is famous for the song 'Jerusalema'?": {
        "options": ["Black Mambazo", "The Soil", "Ladysmith Black Mambazo", "Master KG"],
        "correct": "Master KG"
    },
    "What is the largest ethnic group in South Africa?": {
        "options": ["Zulu", "Xhosa", "Afrikaner", "Sotho"],
        "correct": "Zulu"
    },
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("South African Quiz Game")
        
        self.question_number = 0
        self.score = 0
        self.questions = list(quiz_data.keys())

        # Display the first question
        self.display_question()

    def display_question(self):
        """Display the next question and its options."""
        if self.question_number < len(self.questions):
            question = self.questions[self.question_number]
            options = quiz_data[question]["options"]
            
            # Display the question
            question_label.config(text=question)
            
            # Display options as buttons
            for i, option in enumerate(options):
                option_buttons[i].config(text=option, command=lambda i=i: self.check_answer(options[i]))
            
        else:
            # When all questions are answered
            self.show_result()

    def check_answer(self, selected_answer):
        """Check the selected answer and update score."""
        correct_answer = quiz_data[self.questions[self.question_number]]["correct"]
        
        if selected_answer == correct_answer:
            self.score += 1
        
        # Move to the next question
        self.question_number += 1
        self.display_question()

    def show_result(self):
        """Show the result at the end of the quiz."""
        messagebox.showinfo("Quiz Completed", f"Your score is {self.score}/{len(self.questions)}")
        self.root.quit()

# Set up the main window
root = tk.Tk()

# Create a label to display the question
question_label = tk.Label(root, text="", font=("Arial", 14), width=50, height=3, anchor="w")
question_label.pack(pady=20)

# Create buttons for the answer options
option_buttons = [tk.Button(root, text="", font=("Arial", 12), width=30, height=2) for _ in range(4)]
for button in option_buttons:
    button.pack(pady=5)

# Start the quiz application
quiz_app = QuizApp(root)

# Run the Tkinter event loop
root.mainloop()
