from tkinter import *

root = Tk()
root.title('PYTHON GUI')
root.geometry('640x480') #가로세로

txt = Text(root, width=30, height=5) #여러줄로 입력받을 때
txt.pack()

txt.insert(END, '글자를 입력하세요')

e=Entry(root, width=30) # 한줄로 입력받을 때
e.pack()
e.insert(0, '한줄만 입력')

def btncmd():
    # 내용 출력
    print(txt.get('1.0',END)) # 1.0 -> 1 : 라인 1부터, 0 : 컬럼 0번 부터 
    print(e.get())

    # 내용 삭제
    txt.delete('1.0',END)
    e.delete(0,END)

btn=Button(root,text='클릭',command=btncmd)
btn.pack()

root.mainloop()