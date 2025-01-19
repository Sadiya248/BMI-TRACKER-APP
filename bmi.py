import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        height_in_meters = height * 0.3048
        print(f"Height in meters: {height_in_meters}") 
        
        bmi = weight / (height_in_meters ** 2)
        print(f"BMI: {bmi}")  
        if bmi < 18.5:
            category = "Underweight"
            recommendation = "Focus on gaining weight with a balanced diet and strength training."
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            recommendation = "Maintain your weight with a healthy lifestyle."
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            recommendation = "Consider a balanced diet and regular exercise to lose weight."
        else:
            category = "Obese"
            recommendation = "Consult a healthcare provider for guidance on weight loss."
        
        bmi_label.config(text=f"BMI: {bmi:.2f}")
        category_label.config(text=f"Category: {category}")
        recommendation_label.config(text=f"Recommendation: {recommendation}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

app = tk.Tk()
app.title("BMI Tracker App")
app.geometry("400x300")
app.configure(bg="#D2B48C")


font = ("Helvetica", 14)


tk.Label(app, text="Enter your weight (kg):", bg="#D2B48C", font=font).pack(pady=5)
weight_entry = tk.Entry(app, font=font)
weight_entry.pack(pady=5)


tk.Label(app, text="Enter your height (feet):", bg="#D2B48C", font=font).pack(pady=5)
height_entry = tk.Entry(app, font=font)
height_entry.pack(pady=5)


calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi, font=font)
calculate_button.pack(pady=10)


bmi_label = tk.Label(app, text="BMI: ", bg="#D2B48C", font=font)
bmi_label.pack(pady=5)
category_label = tk.Label(app, text="Category: ", bg="#D2B48C", font=font)
category_label.pack(pady=5)
recommendation_label = tk.Label(app, text="Recommendation: ", bg="#D2B48C", font=font, wraplength=300, justify="center")
recommendation_label.pack(pady=5)

app.mainloop()
