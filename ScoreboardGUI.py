from tkinter import *

root = Tk()  

header = Label(root, text="Track your darts!")

p1 = Label(root, text="Player 1", font=(25))
p2 = Label(root, text="Player 2", font=(25))
p1Score = Label(root, text="[Score]", font=(25))
p2Score = Label(root, text="[Score]", font=(25))

# Create buttons for dartboard segments 

d = Button(text="double")
t = Button(text="triple")

s1 = Button(text="1 ")
s2 = Button(text="2")
s3 = Button(text="3")
s4 = Button(text="4")
s5 = Button(text="5")
s6 = Button(text="6")
s7 = Button(text="7")
s8 = Button(text="8")
s9 = Button(text="9")
s10 = Button(text="10")
s11 = Button(text="11")
s12 = Button(text="12")
s13 = Button(text="13")
s14 = Button(text="14")
s15 = Button(text="15")
s16 = Button(text="16")
s17 = Button(text="17")
s18 = Button(text="18")
s19 = Button(text="19")
s20 = Button(text="20")
s25 = Button(text="25 ring")
bullseye = Button(text="Bullseye")

header.grid(row=0, column=1)

p1.grid(row=0, column=4, padx=50)
p2.grid(row=0, column=5, padx=50) 

d.grid(row=1, column=1, padx=5, pady=5)
t.grid(row=1,column=2,padx=5, pady=5)

p1Score.grid(row=1, column=4, padx=50, pady=5)
p2Score.grid(row=1, column=5, padx=50, pady=5)

s1.grid(row=2, column=0, padx=5, pady=5)
s2.grid(row=2, column=1, padx=5, pady=5)
s3.grid(row=2,column=2, padx=5, pady=5)
s4.grid(row=2,column=3, padx=5, pady=5)

s5.grid(row=3, column=0, padx=5, pady=5)
s6.grid(row=3, column=1, padx=5, pady=5)
s7.grid(row=3,column=2, padx=5, pady=5)
s8.grid(row=3,column=3, padx=5, pady=5)

s9.grid(row=4, column=0, padx=5, pady=5)
s10.grid(row=4, column=1, padx=5, pady=5)
s11.grid(row=4,column=2, padx=5, pady=5)
s12.grid(row=4,column=3, padx=5, pady=5)

s13.grid(row=5, column=0, padx=5, pady=5)
s14.grid(row=5, column=1, padx=5, pady=5)
s15.grid(row=5,column=2, padx=5, pady=5)
s16.grid(row=5,column=3, padx=5, pady=5)

s17.grid(row=6, column=0, padx=5, pady=5)
s18.grid(row=6, column=1, padx=5, pady=5)
s19.grid(row=6,column=2, padx=5, pady=5)
s20.grid(row=6,column=3, padx=5, pady=5)

s25.grid(row=7, column=1, pady=5)
bullseye.grid(row=7, column=2, pady=5)

root.mainloop()