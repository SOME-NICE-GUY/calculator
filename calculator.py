import math
import keyboard
from future.moves import tkinter as tk
from future.moves.tkinter import messagebox

number = ''
theme = 'white'


# calculator functions
# when a number functions is called, that number will be added to the input field
def zero():
    global number, entry
    number = entry.get()
    number += '0'
    # removes and adds the number
    entry.delete(0, tk.END)
    entry.insert(0, number)


def one():
    global number, entry
    number = entry.get()
    number += '1'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def two():
    global number, entry
    number = entry.get()
    number += '2'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def three():
    global number, entry
    number = entry.get()
    number += '3'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def four():
    global number, entry
    number = entry.get()
    number += '4'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def five():
    global number, entry
    number = entry.get()
    number += '5'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def six():
    global number, entry
    number = entry.get()
    number += '6'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def seven():
    global number, entry
    number = entry.get()
    number += '7'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def eight():
    global number, entry
    number = entry.get()
    number += '8'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def nine():
    global number, entry
    number = entry.get()
    number += '9'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def dot():
    global number, entry
    number = entry.get()
    number += '.'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def plus():
    global number, entry
    number = entry.get()
    number += '+'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def minus():
    global number, entry
    number = entry.get()
    number += '-'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def devide():
    global number, entry
    number = entry.get()
    number += '/'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def multiply():
    global number, entry
    number = entry.get()
    number += '*'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def power():
    global number, entry
    number = entry.get()
    number += '**'
    entry.delete(0, tk.END)
    entry.insert(0, number)


def clear():
    global entry
    entry.delete(0, tk.END)


def backspace():
    global entry, number
    try:
        entry.delete(0, tk.END)
        entry.insert(0, number[0:-1])
        number = number[0:-1]
    except TypeError:
        print('the field is empty')


# (
def p_left():
    global number, entry
    number = entry.get()
    number += '('
    entry.delete(0, tk.END)
    entry.insert(0, number)


# )
def p_right():
    global number, entry
    number = entry.get()
    number += ')'
    entry.delete(0, tk.END)
    entry.insert(0, number)


# square root
def s():
    global number, entry
    number = entry.get()
    number += 'sqrt('
    entry.delete(0, tk.END)
    entry.insert(0, number)


# calculates the number with exec() function
def calculate():
    global number, n
    number = entry.get()
    try:
        d = {'sqrt': math.sqrt}
        exec(f"number = round({number}, ndigits=4)", d)
        number = d['number']
        entry.delete(0, tk.END)
        entry.insert(0, number)
    except Exception as e:
        print(f'error: {e}')
        messagebox.showinfo('Error', 'Enter valid numbers and operations')


def info():
    messagebox.showinfo('guide',
                        'Press \'enter\' to calculate\n'
                        'Calculator V3.0 ; updates:\n'
                        '1 press "[" and "]" and they will be displayed as "(" and ")"\n'
                        '2.1 now you can calculate the square root of a number\n'
                        '2.2 press s to add \'sqrt\' to the number\n'
                        '2.3 sqrt stands for \'square root\'\n'
                        '2.4 sqrt(2+2) --> 2 & sqrt(64) --> 8 & sqrt(n**2) --> n\n'
                        '3.1 added the option to change the theme\n'
                        '3.2 press \'d\' to change the theme')


# used for changing the theme.
def change_properties(properties, values):
    b0[properties] = values
    b1[properties] = values
    b2[properties] = values
    b3[properties] = values
    b4[properties] = values
    b5[properties] = values
    b6[properties] = values
    b7[properties] = values
    b8[properties] = values
    b9[properties] = values
    b_dot[properties] = values
    b_plus[properties] = values
    b_minus[properties] = values
    b_multiply[properties] = values
    b_devide[properties] = values
    b_power[properties] = values
    b_bs[properties] = values
    b_info[properties] = values
    b_clear[properties] = values
    b_calculate[properties] = values
    entry[properties] = values


def change_theme():
    global theme
    if theme == 'white':
        theme = 'black'
        canvas['bg'] = 'Black'
        change_properties('bg', 'Black')
        change_properties('fg', 'White')
    else:
        theme = 'white'
        canvas['bg'] = 'white'
        change_properties('bg', 'white')
        change_properties('fg', 'Black')
    print(f'theme changed to {theme}')


# main window
window = tk.Tk()
window.title('simple calculator3')

# size of the window
canvas = tk.Canvas(window, width=300, height=420)
canvas.pack()

# entries and buttons
entry = tk.Entry(text=number, font=('', 17))
canvas.create_window(135, 20, window=entry)

b0 = tk.Button(text=0, font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=zero)
canvas.create_window(30, 90, window=b0)

b1 = tk.Button(text=1, font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=one)
canvas.create_window(90, 90, window=b1)

b2 = tk.Button(text=2, font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=two)
canvas.create_window(150, 90, window=b2)

b3 = tk.Button(text=3, font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=three)
canvas.create_window(210, 90, window=b3)

b4 = tk.Button(text=4, font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=four)
canvas.create_window(270, 90, window=b4)

b5 = tk.Button(text=5, font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=five)
canvas.create_window(30, 180, window=b5)

b6 = tk.Button(text=6, font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=six)
canvas.create_window(90, 180, window=b6)

b7 = tk.Button(text=7, font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=seven)
canvas.create_window(150, 180, window=b7)

b8 = tk.Button(text=8, font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=eight)
canvas.create_window(210, 180, window=b8)

b9 = tk.Button(text=9, font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=nine)
canvas.create_window(270, 180, window=b9)

b_dot = tk.Button(text='.', font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=dot)
canvas.create_window(30, 361, window=b_dot)

b_plus = tk.Button(text='+', font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=plus)
canvas.create_window(30, 270, window=b_plus)

b_minus = tk.Button(text='-', font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=minus)
canvas.create_window(90, 270, window=b_minus)

b_multiply = tk.Button(text='*', font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=multiply)
canvas.create_window(150, 270, window=b_multiply)

b_devide = tk.Button(text='/', font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=devide)
canvas.create_window(210, 270, window=b_devide)

b_power = tk.Button(text='^', font=('', 25), width=2, height=1, relief=tk.RAISED, borderwidth=8, command=power)
canvas.create_window(270, 270, window=b_power)

b_calculate = tk.Button(text='=', font=('', 25), width=3, height=1, relief=tk.RAISED, borderwidth=9, command=calculate)
canvas.create_window(173, 360, window=b_calculate)

b_clear = tk.Button(text='clear', font=('', 16), width=4, height=2, relief=tk.RAISED, borderwidth=9, command=clear)
canvas.create_window(97, 361, window=b_clear)

b_bs = tk.Button(text='back\nspace', font=('', 16), width=5, height=2, relief=tk.RAISED, borderwidth=9,
                 command=backspace)
canvas.create_window(257, 361, window=b_bs)

b_info = tk.Button(text='i', font=('', 16), relief=tk.RAISED, borderwidth=7, command=info)
canvas.create_window(285, 25, window=b_info)

change_properties('bg', 'White')

# shows the info panel
info()

# calls functions when a key in keyboard is pressed
keyboard.on_press_key("enter", lambda _: calculate())
keyboard.on_press_key("0", lambda _: zero())
keyboard.on_press_key("1", lambda _: one())
keyboard.on_press_key("2", lambda _: two())
keyboard.on_press_key("3", lambda _: three())
keyboard.on_press_key("4", lambda _: four())
keyboard.on_press_key("5", lambda _: five())
keyboard.on_press_key("6", lambda _: six())
keyboard.on_press_key("7", lambda _: seven())
keyboard.on_press_key("8", lambda _: eight())
keyboard.on_press_key("9", lambda _: nine())
keyboard.on_press_key(".", lambda _: dot())
keyboard.on_press_key("-", lambda _: minus())
keyboard.on_press_key("+", lambda _: plus())
keyboard.on_press_key("*", lambda _: multiply())
keyboard.on_press_key("/", lambda _: devide())
keyboard.on_press_key("backspace", lambda _: backspace())
keyboard.on_press_key("[", lambda _: p_left())
keyboard.on_press_key("]", lambda _: p_right())
keyboard.on_press_key("delete", lambda _: clear())
keyboard.on_press_key("s", lambda _: s())
keyboard.on_press_key("d", lambda _: change_theme())

# runs the main window
window.mainloop()

# second window, it is just a goodbye window
bye_window = tk.Tk()
bye_window.title('Goodbye')
bye_label = tk.Label(text='Created by Parham', font=0, fg='red', bg='blue')
bye_label.pack()
bye_window.mainloop()
