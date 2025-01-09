import tkinter as tk
from tkinter import ttk

def display_table():
    try:
        number = int(entry_number.get())
        multiples = int(entry_multiples.get())
        result = ""
        for i in range(1, multiples + 1):
            result += f"{number} x {i} = {number * i}\n"
        text_result.config(state="normal")
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
        text_result.config(state="disabled")
    except ValueError:
        text_result.config(state="normal")
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, "Please enter valid numbers!")
        text_result.config(state="disabled")

root = tk.Tk()
root.title("Multiplication Table Generator")
root.geometry("400x700")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

label_header = tk.Label(root, text="Multiplication Table Generator", font=("Helvetica", 16, "bold"), bg="#f4f4f4", fg="#333")
label_header.pack(pady=10)

frame_inputs = tk.Frame(root, bg="#f4f4f4")
frame_inputs.pack(pady=20)

label_number = tk.Label(frame_inputs, text="Enter a number:", font=("Helvetica", 12), bg="#f4f4f4", fg="#333")
label_number.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_number = ttk.Entry(frame_inputs, width=20)
entry_number.grid(row=0, column=1, padx=10, pady=5)

label_multiples = tk.Label(frame_inputs, text="Enter multiples:", font=("Helvetica", 12), bg="#f4f4f4", fg="#333")
label_multiples.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_multiples = ttk.Entry(frame_inputs, width=20)
entry_multiples.grid(row=1, column=1, padx=10, pady=5)

btn_generate = ttk.Button(root, text="Generate Table", command=display_table)
btn_generate.pack(pady=10)

frame_result = tk.Frame(root, bg="#f4f4f4")
frame_result.pack(pady=10, fill="both", expand=True)

text_result = tk.Text(frame_result, width=40, height=15, state="disabled", wrap="word", font=("Courier New", 12))
text_result.pack(pady=10, padx=10, fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_result, command=text_result.yview)
scrollbar.pack(side="right", fill="y")
text_result.config(yscrollcommand=scrollbar.set)

root.mainloop()