from automata.pda.dpda import DPDA
import tkinter as tk
from tkinter import messagebox

dpda = DPDA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    stack_symbols={'$', 'B'},
    transitions={
        'q0': {
            'a': {'$': ('q0', ('B', '$')), 'B': ('q0', ('B', 'B'))},  # transition pushes 'B' to stack
            'b': {'B': ('q1', ('B',))}
        },
        'q1': {
            'b': {'B': ('q2', '')}
        },
        'q2': {
            'b': {'B': ('q1', 'B')},
            '': {'$': ('q3', ('$',))}  # transition does not change stack
        }
    },
    initial_state='q0',
    initial_stack_symbol='$',
    final_states={'q3'},
    acceptance_mode='final_state'
)


def ExitApplication():
    """Exit button function"""
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        quit()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def check_entry_fields():
    """DFA GUI"""
    s_id = language.get()

    if dpda.accepts_input(s_id):
        res.configure(text=str(language.get() + " accepted."))
    else:
        res.configure(text=str(language.get() + " rejected."))


gui = tk.Tk()
gui.geometry("300x135")
gui.title("PDA")

tk.Label(gui, text="Enter PDA: ").pack()
language = tk.Entry(gui)
language.pack()
res = tk.Label(gui)
res.pack()

B2 = tk.Button(gui, text="Exit", command=ExitApplication, activeforeground='White',
               activebackground="blue", bg="white", fg="Black",
               width=500, font='summer', bd=5)

B1 = tk.Button(gui, text="Check", command=check_entry_fields, activeforeground='White',
               activebackground="blue", bg="white", fg="Black",
               width=500, font='summer', bd=5)

B1.pack(side='top')
B2.pack(side='top')

tk.mainloop()
