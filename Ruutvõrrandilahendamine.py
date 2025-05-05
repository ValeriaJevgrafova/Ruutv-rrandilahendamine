import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def solve():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        result_text.configure(bg='white')
    except ValueError:
        result_text.configure(bg='pink')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Viga: täitke kõik väljad korrektselt arvudega.")
        return

    D = b**2 - 4*a*c
    explanation = f"Antud võrrand: {a}x² + {b}x + {c} = 0\n"
    explanation += f"D = {b}² - 4×{a}×{c} = {D}\n"

    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        explanation += "D > 0 → 2 lahendit:\n"
        explanation += f"x₁ = {x1:.4f}\n"
        explanation += f"x₂ = {x2:.4f}"
    elif D == 0:
        x = -b / (2*a)
        explanation += "D = 0 → 1 lahend:\n"
        explanation += f"x = {x:.4f}"
    else:
        explanation += "D < 0 → Lahend puudub (diskriminant on negatiivne)"

    result_text.configure(bg='white')
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, explanation)

def plot_graph():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        messagebox.showerror("Viga", "Täitke koefitsiendid õigesti enne graafiku koostamist.")
        return

    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    plt.figure("Ruutvõrrand")
    plt.title("Ruutvõrrand")
    plt.plot(x, y, 'b.', label='y = ax² + bx + c')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)

    D = b**2 - 4*a*c
    if D >= 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        plt.plot([x1, x2], [0, 0], 'ro')  # lahendid

    vertex_x = -b / (2*a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    plt.plot(vertex_x, vertex_y, 'go')  # tipp

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

# Graafiline liides
root = tk.Tk()
root.title("Ruutvõrrandi lahendamine")

tk.Label(root, text="Sisesta koefitsiendid:").grid(row=0, column=0, columnspan=2)

tk.Label(root, text="a:").grid(row=1, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1)

tk.Label(root, text="b:").grid(row=2, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1)

tk.Label(root, text="c:").grid(row=3, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=3, column=1)

tk.Button(root, text="Lahenda", command=solve).grid(row=4, column=0, pady=5)
tk.Button(root, text="Graafik", command=plot_graph).grid(row=4, column=1)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

