import tkinter as tk

# Function to display data for 10th
def show_10th():
    data = """
    10th Grade:
    - School:  ZPHS
    - Year of Passing: 2018
    - GPA: 9.8
    """
    output_label.config(text=data)

# Function to display data for 12th
def show_12th():
    data = """
    12th Grade:
    - School: Vijaya Kranthi Junior College
    - Year of Passing: 2020
    - GPA: 9.94
    """
    output_label.config(text=data)

# Function to display data for Graduation
def show_graduation():
    data = """
    Graduation:
    - College: sri sarathi institute of engineering and technology
    - Degree: Bachelor of Technology
    - Year of Graduation: 2024
    - CGPA: 8.7
    """
    output_label.config(text=data)

# Creating the main window
root = tk.Tk()
root.title("My Education Details")

# Creating buttons for each educational level
btn_10th = tk.Button(root, text="10th", width=10, height=5, font=("Arial", 14), command=show_10th)
btn_12th = tk.Button(root, text="12th", width=10, height=5, font=("Arial", 14), command=show_12th)
btn_graduation = tk.Button(root, text="Graduation", width=10, height=5, font=("Arial", 14), command=show_graduation)

# Creating a label to display data
output_label = tk.Label(root, text="Select a level to see data", font=("Arial", 14), justify="left", padx=10, pady=10)

# Placing the buttons and label in the window
btn_10th.pack(pady=10)
btn_12th.pack(pady=10)
btn_graduation.pack(pady=10)
output_label.pack(pady=20)

# Running the Tkinter event loop
root.mainloop()
