from tkinter import *
import threading
import ystockquote

top= Tk()
top.title('Stock Tracker')
f1= Frame(top)
f1.pack()

f2= Frame(top)
f2.pack()
t1 = Text(f1, height=8, width=50 )
t1.pack()
e1= Entry(f2)
e1.pack(side= LEFT)
b1= Button(f2, text= "Enter", command = lambda: bton())
b1.pack(side=RIGHT)


def bton():
  stocks = e1.get()
  stock_list = list(map(str,stocks.split()))
  x=0
  while x < len(stock_list):
    data = ystockquote.get_price_book(stock_list[x-1])
    txt = "Current price for {0}: ${1} \n".format(stock_list[x-1],data)
    txt1 = "--------------------------- \n"
    t1.insert(END, txt)
    x+=1
  threading.Timer(900,bton).start()
  t1.insert(END,txt1)
  
top.mainloop()
