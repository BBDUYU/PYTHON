from tkinter import *

root = Tk()
root.title('PYTHON GUI')

btn1=Button(root,text='버튼1')
btn1.pack()

btn2=Button(root,padx=5,pady=10,text='버튼2') # 여백 채우기
btn2.pack()

btn3=Button(root,padx=10,pady=5,text='버튼3')
btn3.pack()

btn4=Button(root,width=10,height=3,text='버튼4') # 정해진 크기
btn4.pack()

btn5=Button(root,fg='red',bg='yellow',text='버튼5')
btn5.pack()

photo=PhotoImage(file='GUI/gui_basic/img.png')
btn6 = Button(root,image=photo)
btn6.pack()

def btncmd():
    print('버튼이 클릭되었습니다')

btn7=Button(root,text='동작',command=btncmd)
btn7.pack()

root.mainloop()