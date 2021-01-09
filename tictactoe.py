import tkinter as tk


x = 'X'
o = 'O'
btnFont = 'Verdana 22'
btns = []
clicks = 0
btnsIndex = 0
root = tk.Tk()
root.config(bg='grey')

b0 = tk.StringVar(); b1 = tk.StringVar(); b2 = tk.StringVar()
b3 = tk.StringVar(); b4 = tk.StringVar(); b5 = tk.StringVar()
b6 = tk.StringVar(); b7 = tk.StringVar(); b8 = tk.StringVar()

mainLayout = {0: b0, 1: b1, 2: b2,
              3: b3, 4: b4, 5: b5,
              6: b6, 7: b7, 8: b8}


def clicked(btn, btnVar):
    global clicks
    if clicks % 2 == 0:
        player = x
    else:
        player = o
    btnVar.set(player)
    btns[btn].config(state='disabled')
    clicks += 1
    win = winCheck(player)
    if win:
        for i in range(len(btns)):
            btns[i].config(state='disabled')
    elif clicks == 9 and win == False:
        print('DRAW')


def winCheck(player):
    for i in range(3):
        if mainLayout.get(i * 3).get() == player and mainLayout.get(i * 3 + 1).get() == player and mainLayout.get(i * 3 + 2).get() == player:
            return True
        elif mainLayout.get(i).get() == player and mainLayout.get(i + 3).get() == player and mainLayout.get(i + 6).get() == player:
            return True
        if i == 0:
            if mainLayout.get(i).get() == player and mainLayout.get(i + 4).get() == player and mainLayout.get(i + 8).get() == player:
                return True
            elif mainLayout.get(i + 6).get() == player and mainLayout.get(i + 4).get() == player and mainLayout.get(i + 2).get() == player:
                return True
    return False


def newGame():
    global clicks
    clicks = 0
    for i in range(len(btns)):
        btns[i].config(state='normal')
        mainLayout.get(i).set('')


menu = tk.Menu(root)
root.config(menu=menu)
subMenu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label='Game', menu=subMenu)
subMenu.add_command(label='New Game', command=newGame)

for i in mainLayout.keys():
    if i <= 2:
        r = 0
        c = i
    elif i >= 3 and i <= 5:
        r = 1
        c = i - 3
    elif i >= 6:
        r = 2
        c = i - 6
    myBtn = tk.Button(root, textvariable=mainLayout.get(i), width=3, height=2, font=btnFont, 
                      command=lambda btn=btnsIndex, btnVar=mainLayout.get(i): clicked(btn, btnVar))
    myBtn.grid(row=r, column=c, padx=5, pady=5)
    btns.append(myBtn)
    btnsIndex += 1


root.mainloop()
