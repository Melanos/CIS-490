from automata.tm.dtm import DTM
import tkinter as tk
from tkinter import messagebox

dtm = DTM(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    transitions={
        'q0': {
            '0': ('q0', '1', 'R'),
            '1': ('q0', '0', 'R'),
            'B': ('q1', 'B', 'L')
        },
        'q1': {
            '0': ('q1', '0', 'L'),
            '1': ('q1', '1', 'L'),
            'B': ('q2', 'B', 'R')
        }
    },
    initial_state='q0',
    blank_symbol='B',
    final_states={'q2'}
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

    if dtm.accepts_input(s_id):
        res.configure(text=str(language.get() + " accepted."))
    else:
        res.configure(text=str(language.get() + " rejected."))


gui = tk.Tk()
gui.geometry("300x135")
gui.title("TM")

tk.Label(gui, text="Enter TM: ").pack()
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
