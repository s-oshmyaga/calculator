""" Вывод внешнего вида калькулятора """
from tkinter import *


def calculator(value):
    if value.isdigit() or value in '+-*/%':
        display_text.insert(END, value)
    elif value == 'C':
        display_text.delete(END)
    elif value == '()':
        # выводит всегда *(
        last_sign = display_text.get('0.end')
        if last_sign.isdigit() or last_sign in '%':
            display_text.insert(END, '*(')
        elif last_sign in '+ (*/-':
            display_text.insert(END, '(')
        else:
            display_text.insert(END, ')')
    elif value == '.':
        last_sign = display_text.get('0.end')
        # всегда выводит 0.
        if last_sign in ['0123456789']:
            display_text.insert('0.end', '.')
        else:
            display_text.insert('0.end', '0.')


window = Tk()
window.title('Calculator')
window.geometry('400x310')

for i in range(2):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)


buttons_list = ['=', 'C', '%', '()', '/', '*', '+', '-', '.', u'\u221a',
                '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
buttons_list = iter(buttons_list)


def buttons():
    for k in range(4):
        frame = Frame(master=window, relief='raised', borderwidth=3)
        frame.grid(row=k+1, sticky='nsew')
        for _ in range(5):
            button_value = next(buttons_list)
            cmd = lambda x=button_value: calculator(x)
            btn = Button(text=button_value, master=frame, command=cmd, height=2, width=2)
            btn.pack(side=LEFT, fill=BOTH, expand=True)


display_text = Text(master=window, fg='green', bg='black',
                    height=4, font='Arial 16')
display_text.grid(row=0, sticky='nsew')


def master():
    buttons()
    window.mainloop()


master()
