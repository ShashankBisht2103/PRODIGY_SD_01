import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- Conversion Function ---------------- #

def convert_temperature():
    try:
        temp = float(temp_entry.get())
        unit = unit_var.get()

        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15

            result = f"""Fahrenheit : {fahrenheit:.2f} °F
Kelvin      : {kelvin:.2f} K"""

        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15

            result = f"""Celsius     : {celsius:.2f} °C
Kelvin      : {kelvin:.2f} K"""

        elif unit == "Kelvin":
            if temp < 0:
                messagebox.showerror(
                    "Invalid Temperature",
                    "Kelvin cannot be less than 0."
            )
            return
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32

            result = f"""Celsius     : {celsius:.2f} °C
Fahrenheit : {fahrenheit:.2f} °F"""

        result_label.config(text=result)

    except ValueError:
        messagebox.showerror(
        "Invalid Input",
        "Please enter a valid numeric temperature."
    )
    temp_entry.focus_set()
    
def clear_fields():
    temp_entry.delete(0, tk.END)
    unit_dropdown.current(0)
    result_label.config(text="Converted values will appear here.")

# ---------------- Main Window ---------------- #

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("500x450")
root.resizable(False, False)
root.configure(bg="#F5F7FA")

title = tk.Label(
    root,
    text="🌡 Temperature Converter",
    font=("Segoe UI", 20, "bold"),
    bg="#F5F7FA",
    fg="#1E3A8A"
)
title.pack(pady=20)

tk.Label(
    root,
    text="Enter Temperature:",
    font=("Segoe UI",12),
    bg="#F5F7FA"
).pack()

temp_entry = tk.Entry(root,font=("Arial",14),width=20)
temp_entry.pack(pady=10)

tk.Label(
    root,
    text="Select Unit:",
    font=("Segoe UI",12),
    bg="#F5F7FA"
).pack()

unit_var = tk.StringVar()

unit_dropdown = ttk.Combobox(
    root,
    textvariable=unit_var,
    values=["Celsius","Fahrenheit","Kelvin"],
    state="readonly",
    font=("Arial",12)
)

unit_dropdown.current(0)
unit_dropdown.pack(pady=10)

convert_btn = tk.Button(
    root,
    text="Convert",
    font=("Segoe UI",12,"bold"),
    width=15,
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    command=convert_temperature
)

convert_btn.pack(pady=20)

clear_btn = tk.Button(
    root,
    text="Clear",
    font=("Segoe UI",12,"bold"),
    width=15,
    bg="#DC2626",
    fg="white",
    activebackground="#B91C1C",
    activeforeground="white",
    relief="flat",
    command=clear_fields
)

clear_btn.pack(pady=5)

result_label = tk.Label(
    root,
    text="Converted values will appear here.",
    font=("Segoe UI",12),
    bg="#F5F7FA",
    fg="#111827",
    justify="left"
)

result_label.pack(pady=20)
root.bind("<Return>", lambda event: convert_temperature())
temp_entry.focus_set()
root.mainloop()