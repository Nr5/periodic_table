from tkinter import Tk, Canvas, Frame
from random import shuffle

root = Tk()
frame=Frame(root)
elements=[]
colors=["blue","green","yellow","orange","red","brown","purple","darkred","grey","darkblue","white"]
group=0
rects=[]
with open ("elements.txt") as f:
    for n,line  in enumerate(f):
        elements += [[n]+line.split()]


#elements=list(filter(lambda x:x[3]=="5",elements))
shuffle(elements)
canvas = Canvas(frame,height=500,width=50*32)
errors=0
textfield=canvas.create_text(600,400,fill="darkblue",font="Times 20",text= elements[0][1])
errorfield=canvas.create_text(100,400,fill="red",font="Times 20",text= "0")
jumpfield=canvas.create_rectangle(0,450,50*32,500,fill="yellow" )
def getcoords(nr):
    j=nr+30*(nr>0)+24*(nr>3)+24*(nr>11)+14*(nr>20)+14*(nr>38)
    return (j%32)*50, (j//32)*50
    

    
def callback(event):
    
    global elements
    global errors
    
    if event.y>450:
        elements = elements[1:] + [ elements[0] ]
        canvas.itemconfigure(textfield, text=elements[0][1] )
        return
    if not elements: return
    pos=event.x//50 + (event.y//50)*32
    if (pos>0 and pos < 31) or (pos>33 and pos< 58) or (pos>65 and pos< 90) or (pos > 98 and pos < 113) or (pos > 130 and pos < 145) :
        return
    pos -= 30* (pos>0)  
    pos -= 24* (pos>3) 
    pos -= 24* (pos>11)
    pos -= 14* (pos>20) 
    pos -= 14* (pos>38)
    if pos == elements[0][0]:
        x, y=getcoords(elements[0][0])
        canvas.create_text(x+20,y+20,fill="black",font="Times 20",text= elements[0][2])

        elements= elements[1:] if (len(elements)>1) else 0
        canvas.itemconfigure(textfield, text=elements[0][1] if elements else "you win")
    else:
        errors+=1
    canvas.itemconfigure(errorfield, text=str(errors))
        
for i in elements:
    x, y=getcoords(i[0])
    canvas.create_rectangle(x,y,x+50,y+50,fill=colors[int(i[3])] )

canvas.bind("<Button-1>", callback)

frame.pack()
canvas.pack()

root.mainloop()
