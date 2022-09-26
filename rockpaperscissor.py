#from ast import pack_forget
#from cProfile import label
from tkinter import *
from random import randint
from tkinter.font import BOLD, ITALIC
root=Tk()
root.title("ROCK/PAPER/SCISSORS game")
root.geometry('600x700')
text_lable=Label(root,text="Choose what u want to show:",font=("Arial",28),bg="Red")
text_lable.pack(pady=20)
rock=PhotoImage(file='C:\\Users\\rakes\\Desktop\\images\\rock.png')
paper=PhotoImage(file='C:\\Users\\rakes\\Desktop\\images\\paper.png')
scissor=PhotoImage(file='C:\\Users\\rakes\\Desktop\\images\\scissor.png')
#text_lable.pack(pady=20)
#change bg color
#root.config(bg="white")
pick_number=randint(0,2)
image_list=[rock,paper,scissor]
#fucntion to clear the screen
#def assign():
 #   global play
  #  play=1
def Tie():
    text_draw=Label(root,text="Its a TIE!!!...",font=("Forte",30,BOLD,ITALIC),background="Light Yellow").grid(column=1,row=11) 
def You_win():
    text_draw=Label(root,text="You Win...\nWell Played..!!  ",font=("Comic Sans MS",24,BOLD,ITALIC),background="Green").grid(column=1,row=11)
def You_lose():
    text_draw=Label(root,text="You Lose...",font=("Comic Sans MS",28,BOLD,ITALIC),background="Red").grid(column=1,row=11)
#def choose():
 #   cho_again=Button(root,text="PLAY AGAIN",font=("Arial Rounded MT Bold",25,ITALIC),bd=7,bg="Grey",command=assign).grid(column=1,row=12)
def clear():
    text_lable.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
def action1():
    clear()
    image_rock=Label(root,image=rock).grid(column=0,row=10)
    text_vs=Label(root,text="  VS  ",font=("Arcadia",35),foreground="Red",background="Yellow").grid(column=1,row=10)
    image_random=Label(root,image=image_list[pick_number]).grid(column=2,row=10)
    # rock==0,paper==1,scissor==2
    if (pick_number==0):
        Tie()
    elif(pick_number==1):
        You_lose()
    elif(pick_number==2):
        You_win()
def action2():
    clear()
    image_paper=Label(root,image=paper).grid(column=0,row=10)
    text_vs=Label(root,text="  VS  ",font=("Arcadia",35),foreground="Red",background="Yellow").grid(column=1,row=10)
    image_random=Label(root,image=image_list[pick_number]).grid(column=2,row=10)
    # rock==0,paper==1,scissor==2
    if (pick_number==1):
        Tie()
    elif(pick_number==2):
        You_lose()
    elif(pick_number==1):
        You_win()
def action3():
    clear()
    image_scissor=Label(root,image=scissor).grid(column=0,row=10)
    text_vs=Label(root,text="  VS  ",font=("Arcadia",35),foreground="Red",background="Yellow").grid(column=1,row=10)
    image_random=Label(root,image=image_list[pick_number]).grid(column=2,row=10)
    # rock==0,paper==1,scissor==2
    if (pick_number==2):
        Tie()
    elif(pick_number==0):
        You_lose()
    elif(pick_number==1):
        You_win()        
#show image as button option to choose between rock paper and scissor.
#play=1
#while(play==1):
 #   global button1,button2,button3    
button1=Button(root,image=rock,borderwidth=0,bd=5,bg="Grey",command=action1)
button2=Button(root,image=paper,borderwidth=0,bd=5,bg="Grey",command=action2)
button3=Button(root,image=scissor,borderwidth=0,bd=5,bg="Grey",command=action3)
button1.pack(pady=20)
button2.pack(pady=20)
button3.pack(pady=20)
    #choose()
    #clear()

#play()

root.mainloop()