from tkinter import *

root = Tk()
root.title('PYTHON GUI')
root.geometry('640x480') #가로세로

listbox = Listbox(root,selectmode='extended', height=0)
listbox.insert(0,'사과')
listbox.insert(1,'딸기')
listbox.insert(2,'바나나')

listbox.insert(END,'수박')
listbox.insert(END,'포도')
listbox.pack()


def btncmd():
    # 삭제
    #listbox.delete(END) # END : 맨 뒤에 항목을 삭제,  0: 맨 앞 항목을 삭제

    # 갯수
    #print('리스트에는', listbox.size(),'개가 있다')

    # 항목 확인 (시작 idx, 끝 idx)
    print('1번째 부터 3번째 까지의 항목 : ',listbox.get(0,2))

    # 선택된 항목 확인
    print('선택된 항목',listbox.curselection())


btn=Button(root,text='클릭',command=btncmd)
btn.pack()

root.mainloop()