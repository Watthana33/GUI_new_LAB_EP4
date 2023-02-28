from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser

import csv

def writecsv_cost(datalist):
    with open('data_cost.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']

def writecsv_receive(datalist1):
    with open('data_receive.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist1) # datalist = ['pen','pencil','eraser']

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data

GUI = Tk()                  #หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกรายรับ รายจ่าย')#ชื่อโปรแกรม
GUI.geometry('500x400')     #ความกว้างของโปรแกรม


L1 = Label(GUI,text='โปรแกรมบันทึกรายรับ รายจ่าย',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

LF1 = ttk.Labelframe(GUI,text='รายจ่าย')
LF1.place(x=100,y=80)

v_data = StringVar()#ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(ipadx=20,ipady=10)

LF2 = ttk.Labelframe(GUI,text='รายรับ')
LF2.place(x=100,y=180)

v_data2 = StringVar()#ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E2 = ttk.Entry(LF2,textvariable=v_data2,font=('Angsana New',25))
E2.pack(ipadx=20,ipady=10)


################
'''def Button2():
    text = 'บาท'
    messagebox.showinfo('เปิดระบบ',text) 

FB2 = Frame(GUI)
FB2.place(x=375,y=160)
B2 = ttk.Button(FB2,text='คำนวณเงินทอน',command=Button2)
B2.pack(ipadx=20,ipady=10)
#B2.place(x=50,y=200)'''
##############

from datetime import datetime

def Savedata():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    data2 = v_data2.get()
    text = [t,data]#[เวลา,ข้อมูลที่ได้จากการกรอก]
    text1 = [t,data2]
    writecsv_cost(text)#บันทึกลง csv
    writecsv_receive(text1)
    v_data.set('')
    v_data2.set('')

def Button2():
    text = 'บันทึกแล้ว'
    messagebox.showinfo('บันทึกแล้ว',text) 
FB2 = Frame(GUI)
FB2.place(x=180,y=280)
B2 = ttk.Button(FB2,text='บันทึก',command=Savedata)
B2.pack(ipadx=20,ipady=10)



GUI.mainloop()
