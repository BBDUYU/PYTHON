import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('PYTHON GUI')
root.geometry('640x480') #가로세로

values=[str(i) + '일' for i in range(1,32)] # 1 ~ 31

readonly_combobox = ttk.Combobox(root, height=5, values=values,state='readonly')
readonly_combobox.current(0)
readonly_combobox.pack() 


combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('카드 결제일') # 최초 목록 제목설정

def btncmd():
    print(readonly_combobox.get())
    print(combobox.get())


btn=Button(root,text='주문',command=btncmd)
btn.pack()

root.mainloop()