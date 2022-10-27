from tkinter import *
from tkinter import messagebox


def click(x):
    global calc_text
    calc_text = calc_text + str(x)
    calc_label.set(calc_text)


def equals():
    global calc_text
    try:
        result = str(eval(calc_text))
        calc_text = result
        calc_label.set(calc_text)
    except ZeroDivisionError:
        messagebox.showerror(message='You can\'t divide by 0!')
    except SyntaxError:
        if calc_text[0] == '0':
            calc_text = calc_text[1:len(calc_text)]
            result = str(eval(calc_text))
            calc_text = result
            calc_label.set(calc_text)
        else:
            messagebox.showerror(message='You can\'t do that! :P')
    except ValueError:
        messagebox.showerror(message='You can\'t do that! :P')


def clear():
    global calc_text
    calc_text = ''
    calc_label.set(calc_text)


def to_square():
    global calc_text
    try:
        result = float(calc_text) * float(calc_text)
        calc_label.set(str(result))
    except ValueError:
        messagebox.showerror(message='You can\'t do that! :P')


def change_sign():
    global calc_text
    try:
        result = float(calc_text)
        result = - result
        calc_text = f'{result}'
    except ValueError:
        messagebox.showerror(message='You can\'t change the sign! :P')
    calc_label.set(calc_text)


def power():
    global calc_text
    calc_text = calc_text + '**'
    calc_label.set(calc_text)


def factorial():
    global calc_text
    result = 1
    try:
        if int(calc_text) < 0:
            messagebox.showerror(message='You can\'t factorial that! :P')
        else:
            for i in range(1, int(calc_text) + 1):
                result *= i
            calc_label.set(str(result))
    except ValueError:
        messagebox.showerror(message='You can\'t factorial that! :P')


def erase():
    global calc_text
    calc_text = calc_text[:-1]
    calc_label.set(calc_text)


root = Tk()

root.title('GT\'S CALCULATOR')
root.iconbitmap('calc.ico')
root.geometry('545x780')

calc_text = ''
calc_label = StringVar()
label = Label(root, font=('Courier', 25, 'bold'), bg='#9fc5e8', width=26, bd=10, relief=SUNKEN,
              textvariable=calc_label, height=3)
label.grid(row=0, column=0, columnspan=4)

button_frame = Frame(root)
button_frame.grid(row=1, column=0, rowspan=5, columnspan=4)
square_button = Button(button_frame, text='x^2', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                       font=('Courier', 25, 'bold'), command=to_square)
square_button.grid(row=1, column=0)
power_button = Button(button_frame, text='x^y', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                      font=('Courier', 25, 'bold'), command=power)
power_button.grid(row=1, column=1)
factorial_button = Button(button_frame, text='x!', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                          font=('Courier', 25, 'bold'), command=factorial)
factorial_button.grid(row=1, column=2)
divide_button = Button(button_frame, text='/', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                       font=('Courier', 25, 'bold'), command=lambda: click('/'))
divide_button.grid(row=1, column=3)
seven_button = Button(button_frame, text='7', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                      font=('Courier', 25, 'bold'), command=lambda: click(7))
seven_button.grid(row=2, column=0)
eight_button = Button(button_frame, text='8', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                      font=('Courier', 25, 'bold'), command=lambda: click(8))
eight_button.grid(row=2, column=1)
nine_button = Button(button_frame, text='9', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                     font=('Courier', 25, 'bold'), command=lambda: click(9))
nine_button.grid(row=2, column=2)
x_button = Button(button_frame, text='X', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                  font=('Courier', 25, 'bold'), command=lambda: click('*'))
x_button.grid(row=2, column=3)
four_button = Button(button_frame, text='4', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                     font=('Courier', 25, 'bold'), command=lambda: click(4))
four_button.grid(row=3, column=0)
five_button = Button(button_frame, text='5', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                     font=('Courier', 25, 'bold'), command=lambda: click(5))
five_button.grid(row=3, column=1)
six_button = Button(button_frame, text='6', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                    font=('Courier', 25, 'bold'), command=lambda: click(6))
six_button.grid(row=3, column=2)
minus_button = Button(button_frame, text='-', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                      font=('Courier', 25, 'bold'), command=lambda: click('-'))
minus_button.grid(row=3, column=3)
one_button = Button(button_frame, text='1', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                    font=('Courier', 25, 'bold'), command=lambda: click(1))
one_button.grid(row=4, column=0)
two_button = Button(button_frame, text='2', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                    font=('Courier', 25, 'bold'), command=lambda: click(2))
two_button.grid(row=4, column=1)
three_button = Button(button_frame, text='3', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                      font=('Courier', 25, 'bold'), command=lambda: click(3))
three_button.grid(row=4, column=2)
plus_button = Button(button_frame, text='+', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                     font=('Courier', 25, 'bold'), command=lambda: click('+'))
plus_button.grid(row=4, column=3)
sign_button = Button(button_frame, text='+/-', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                     font=('Courier', 25, 'bold'), command=change_sign)
sign_button.grid(row=5, column=0)
zero_button = Button(button_frame, text='0', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                     font=('Courier', 25, 'bold'), command=lambda: click(0))
zero_button.grid(row=5, column=1)
dot_button = Button(button_frame, text='.', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                    font=('Courier', 25, 'bold'), command=lambda: click('.'))
dot_button.grid(row=5, column=2)
equal_button = Button(button_frame, text='=', width=6, height=2, bd=4, relief=RAISED, bg='#bad3ea',
                      font=('Courier', 25, 'bold'), command=equals)
equal_button.grid(row=5, column=3)
parleft_button = Button(button_frame, text='(', width=6, height=2, bd=4, relief=SUNKEN, bg='#bad3ea',
                        font=('Courier', 25, 'bold'), command=lambda: click('('))
parleft_button.grid(row=6, column=0)
parright_button = Button(button_frame, text=')', width=6, height=2, bd=4, relief=SUNKEN, bg='#bad3ea',
                         font=('Courier', 25, 'bold'), command=lambda: click(')'))
parright_button.grid(row=6, column=1)
clear_button = Button(button_frame, text='clear', width=6, height=2, bd=4, relief=SUNKEN, bg='#bad3ea',
                      font=('Courier', 25, 'bold'), command=clear)
clear_button.grid(row=6, column=2)
erase_button = Button(button_frame, text='erase', width=6, height=2, bd=4, relief=SUNKEN, bg='#bad3ea',
                      font=('Courier', 25, 'bold'), command=erase)
erase_button.grid(row=6, column=3)

root.mainloop()
