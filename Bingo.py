import random as ran
from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.title("Bingo")
root.geometry("1300x650")
root.configure(background='light cyan')
global buttons
global values
global turn
global e1
global submit1
global e2
global submit2
global check1
global check2
global alltickets
global allbuttons
global tick
tick = [[], []]
for i in range(0, 2):
    for j in range(0, 25):
        tick[i].append(0)
allbuttons = []
alltickets = []
turn = 0
values = []


def generateticket(start, window, no):
    ticket = []
    for i in range(0, 5):
        for j in range(0, 5):
            x = ran.randint(15*i + 1, 15*i + 15)
            while x in ticket:
                x = ran.randint(15*i + 1, 15*i + 15)
            ticket.append(x)
    alltickets.append(ticket)
    printticket(ticket, start, window, no)


def click(window, value, num, tno):
    global values
    global allbuttons
    if value not in values:
        label = Label(window, text="Number has not been called yet", fg="red", bg='light cyan')
        label.grid(row=69, column=70, columnspan=5)
        label.after(5000, lambda: destroy(label))
    else:
        allbuttons[tno][num].config(bg='red')
        tick[tno][num] = 1


def check(value, pno):
    lines = []
    for i in range(0, 5):
        line = 0
        for j in range(0, 5):
            if alltickets[value][5*i + j] in values and tick[pno][5*i + j] == 1:
                line += 1
        lines.append(line)
    for j in range(0, 5):
        line = 0
        for i in range(0, 5):
            if alltickets[value][5*i + j] in values and tick[pno][5*i + j] == 1:
                line += 1
        lines.append(line)
    line = 0
    for i in range(0, 5):
        if alltickets[value][6*i] in values and tick[pno][6*i] == 1:
                line += 1
    lines.append(line)
    line = 0
    for i in range(0, 5):
        j = 4-i
        if alltickets[value][5*i + j] in values and tick[pno][5*i + j] == 1:
                line += 1
    lines.append(line)
    if lines.count(5) >= 5:
        x = msg.showinfo("End of Game", "Player {} wins".format(pno+1))
        if x == 'ok':
            root.quit()


def destroy(e):
    e.destroy()


def getvalue(window, start, mod, x):
    global e1
    global submit1
    global e2
    global submit2
    global values
    try:
        if x == 1:
            a = int(e1.get())
            e1.delete(0, END)
        else:
            a = int(e2.get())
            e2.delete(0, END)
    except ValueError:
        label = Label(window, text="Not a Number", fg="red", bg='light cyan')
        label.grid(row=start[1] - 1, column=start[0], columnspan=5)
        label.after(5000, lambda: destroy(label))
    else:
        if a in values:
            label = Label(window, text="Number can only be called once", fg="red", bg='light cyan')
            label.grid(row=start[1] - 1, column=start[0], columnspan=5)
            label.after(5000, lambda: destroy(label))
        elif 0 < a <= 75:
            global turn
            values.append(a)
            turn += 1
            if turn % 2 == mod:
                e1.config(state=NORMAL)
                submit1.config(state=NORMAL)
                e2.config(state=DISABLED)
                submit2.config(state=DISABLED)
                e1.focus_set()
            else:
                e2.config(state=NORMAL)
                submit2.config(state=NORMAL)
                e1.config(state=DISABLED)
                submit1.config(state=DISABLED)
                e2.focus_set()
            if len(values) >= 75:
                x = msg.showinfo("End of Game", "All values have been called")
                if x == 'ok':
                    root.quit()
        else:
            label = Label(window, text="Number not in Range 0 to 75", fg="red", bg='light cyan')
            label.grid(row=start[1] - 1, column=start[0], columnspan=5)
            label.after(5000, lambda: destroy(label))


def printticket(ticket, start, window, no):
    button.destroy()
    global buttons
    global turn
    buttons = []
    canvas1 = Canvas(window, height=start[1], width=start[0], bg='light cyan', highlightthickness=0)
    canvas2 = Canvas(window, height=start[1], width=start[0], bg='light cyan', highlightthickness=0)
    button_1 = Button(window, text=str(ticket[0]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[0], 0, no))
    button_2 = Button(window, text=str(ticket[1]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[1], 1, no))
    button_3 = Button(window, text=str(ticket[2]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[2], 2, no))
    button_4 = Button(window, text=str(ticket[3]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[3], 3, no))
    button_5 = Button(window, text=str(ticket[4]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[4], 4, no))
    button_6 = Button(window, text=str(ticket[5]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[5], 5, no))
    button_7 = Button(window, text=str(ticket[6]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[6], 6, no))
    button_8 = Button(window, text=str(ticket[7]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[7], 7, no))
    button_9 = Button(window, text=str(ticket[8]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[8], 8, no))
    button_10 = Button(window, text=str(ticket[9]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[9], 9, no))
    button_11 = Button(window, text=str(ticket[10]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[10], 10, no))
    button_12 = Button(window, text=str(ticket[11]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[11], 11, no))
    button_13 = Button(window, text=str(ticket[12]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[12], 12, no))
    button_14 = Button(window, text=str(ticket[13]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[13], 13, no))
    button_15 = Button(window, text=str(ticket[14]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[14], 14, no))
    button_16 = Button(window, text=str(ticket[15]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[15], 15, no))
    button_17 = Button(window, text=str(ticket[16]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[16], 16, no))
    button_18 = Button(window, text=str(ticket[17]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[17], 17, no))
    button_19 = Button(window, text=str(ticket[18]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[18], 18, no))
    button_20 = Button(window, text=str(ticket[19]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[19], 19, no))
    button_21 = Button(window, text=str(ticket[20]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[20], 20, no))
    button_22 = Button(window, text=str(ticket[21]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[21], 21, no))
    button_23 = Button(window, text=str(ticket[22]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[22], 22, no))
    button_24 = Button(window, text=str(ticket[23]), padx=40, pady=20, bg='lemon chiffon', activebackground='yellow', command=lambda: click(window, ticket[23], 23, no))
    button_25 = Button(window, text=str(ticket[24]), padx=40, pady=20, bg='mistyrose', activebackground='yellow', command=lambda: click(window, ticket[24], 24, no))
    buttons.append(button_1)
    buttons.append(button_2)
    buttons.append(button_3)
    buttons.append(button_4)
    buttons.append(button_5)
    buttons.append(button_6)
    buttons.append(button_7)
    buttons.append(button_8)
    buttons.append(button_9)
    buttons.append(button_10)
    buttons.append(button_11)
    buttons.append(button_12)
    buttons.append(button_13)
    buttons.append(button_14)
    buttons.append(button_15)
    buttons.append(button_16)
    buttons.append(button_17)
    buttons.append(button_18)
    buttons.append(button_19)
    buttons.append(button_20)
    buttons.append(button_21)
    buttons.append(button_22)
    buttons.append(button_23)
    buttons.append(button_24)
    buttons.append(button_25)
    canvas1.grid(row=0, column=0, columnspan=start[1], rowspan=start[0])
    canvas2.grid(row=start[0] + 5, column=start[1] + 5, columnspan=start[1], rowspan=start[0])
    e1.grid(row=70, column=71, columnspan=3)
    e1.focus_set()
    submit1.grid(row=70, column=74, columnspan=2)
    e2.grid(row=70, column=71, columnspan=3)
    submit2.grid(row=70, column=74, columnspan=2)
    check1.grid(row=76, column=70, columnspan=5)
    check2.grid(row=76, column=70, columnspan=5)
    label1.grid(row=20, column=71, columnspan=3)
    label2.grid(row=20, column=71, columnspan=3)
    for i in range(0, 5):
        for j in range(0, 5):
            buttons[5*i + j].grid(row=start[0] + j + 1, column=start[1] + i)
    allbuttons.append(buttons)


mod = 0
frame1 = LabelFrame(root, padx=5, pady=5, bd=0, bg='light cyan')
frame1.grid(column=0, row=0)
frame2 = LabelFrame(root, padx=5, pady=5, bd=0, bg='light cyan')
frame2.grid(column=205, row=0)
e1 = Entry(frame1, width=40, bd=2, font=("Arial", 10), borderwidth=5)
submit1 = Button(frame1, text="Enter", bg='gold', bd=2, font=("Arial", 10), command=lambda: getvalue(frame1, [70, 70], mod, 1))
e2 = Entry(frame2, width=40, borderwidth=5, bd=2, font=("Arial", 10), state=DISABLED)
submit2 = Button(frame2, text="Enter", bg='gold', state=DISABLED, bd=2, font=("Arial", 10), command=lambda: getvalue(frame2, [70, 70], mod, 2))
check1 = Button(frame1, text="Check", bg='gold', font=("Arial", 10), width=25, bd=2, padx=5, pady=5, command=lambda: check(0, 0))
check2 = Button(frame2, text="Check", bg='gold', width=25, bd=2, padx=5, pady=5, font=("Arial", 10), command=lambda: check(1, 1))
label1 = Label(frame1, text="Player 1", font=("Arial", 24), bg='light cyan')
label2 = Label(frame2, text="Player 2", font=("Arial", 24),  bg='light cyan')
button = Button(root, text="Start Game", padx=40, pady=20, activebackground='pink', bg='SteelBlue1', font=('Ariel', 25), command=lambda: [generateticket([70, 70], frame1, 0), generateticket([70, 70], frame2, 1)])
button.grid(column=1, row=1, padx=550, pady=270)
root.mainloop()
