from tkinter import *
from app import logics


def calculator(value):
    if value.isdigit() or value in ('+', '-', u'\u03C0', u'\u2236', u'\u2217',
                                    '(', ')', '!'):
        display_text.insert(END, value)
    elif value == 'C':
        display_text.delete('0', END)
    elif value == u'\u2190':
        display_text.delete(len(display_text.get())-1)
    elif value == 'ln':
        last_sign = display_text.get()
        if (last_sign and last_sign[-1].isdigit()) or last_sign == ')':
            display_text.insert(END, '*ln(')
        else:
            display_text.insert(END, 'ln(')
    elif value == '^' or value == u'\u221a':
        display_text.insert(END, value+'(')
    elif value == '.':
        last_sign = display_text.get()[-1]
        if last_sign.isdigit():
            display_text.insert(END, '.')
        else:
            display_text.insert(END, '0.')
    elif value == '=':
        string = display_text.get()
        result = logics.solution(string)
        display_text.delete('0', END)
        display_text.insert('0', result)


window = Tk()
window.title('Calculator')
window.geometry('250x350')

for i in range(2):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)


buttons_list = ['=', 'C', u'\u2190', 'ln', '^', '!', u'\u03C0', '(', ')', u'\u2236', u'\u2217', '+', '-',
                '.', u'\u221a', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
buttons_list = iter(buttons_list)


def buttons():
    for k in range(5):
        frame = Frame(master=window, relief='raised', borderwidth=3)
        frame.grid(row=k+1, sticky='nsew')
        for _ in range(5):
            button_value = next(buttons_list)
            cmd = lambda x = button_value: calculator(x)
            btn = Button(text=button_value, master=frame, command=cmd, height=2, width=2)
            btn.pack(side=LEFT, fill=BOTH, expand=True)


display_text = Entry(master=window, fg='green', bg='black',
                     font='Arial 18')
display_text.grid(row=0, sticky='nsew')


def master():
    buttons()
    window.mainloop()


master()
