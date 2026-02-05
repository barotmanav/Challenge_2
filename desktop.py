import tkinter as tk
from tkinter import scrolledtext, messagebox

from main import run_research, render_final_output, build_llm

def run_task():
    task = task_input.get("1.0", tk.END).strip()

    if not task:
        messagebox.showwarning("Input Required", "Please enter a research task.")
        return

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Running research...\n\n")
    root.update()

    try:
        synthesis, decision = run_research(task)

        final_text = render_final_output(synthesis)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, final_text)

        output_box.insert(tk.END, "\n\n---\nSYSTEM DECISION\n")
        output_box.insert(tk.END, str(decision))

    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error occurred:\n{e}")


root = tk.Tk()
root.title("Collaborative AI Research Dashboard")
root.geometry("900x600")


tk.Label(root, text="Research Task").pack(anchor="w", padx=10, pady=(10, 0))
task_input = scrolledtext.ScrolledText(root, height=4)
task_input.pack(fill="x", padx=10, pady=5)
tk.Button(root, text="Run Research", command=run_task).pack(pady=10)

tk.Label(root, text="Research Output").pack(anchor="w", padx=10)
output_box = scrolledtext.ScrolledText(root, height=20)
output_box.pack(fill="both", expand=True, padx=10, pady=(5, 10))


root.mainloop()
