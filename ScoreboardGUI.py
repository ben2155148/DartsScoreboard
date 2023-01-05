from tkinter import *

root = Tk()
root.title("Darts Scoreboard")

p1 = Label(root, text="Player 1", font=(25))
p2 = Label(root, text="Player 2", font=(25))
p1ScoreLabel = Label(root, text=301, font=(25))
p2ScoreLabel = Label(root, text=301, font=(25))

# Create buttons for dartboard segments
d = Button(text="double")
t = Button(text="triple")

s1 = Button(text="1")
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
s25 = Button(text="25 Ring")
bullseye = Button(text="Bullseye")

p1.grid(row=0, column=4)
p2.grid(row=0, column=5)

d.grid(row=1, column=1)
t.grid(row=1, column=2)

p1ScoreLabel.grid(row=1, column=4)
p2ScoreLabel.grid(row=1, column=5)

s1.grid(row=2, column=0)
s2.grid(row=2, column=1)
s3.grid(row=2, column=2)
s4.grid(row=2, column=3)

s5.grid(row=3, column=0)
s6.grid(row=3, column=1)
s7.grid(row=3, column=2)
s8.grid(row=3, column=3)

s9.grid(row=4, column=0)
s10.grid(row=4, column=1)
s11.grid(row=4, column=2)
s12.grid(row=4, column=3)

s13.grid(row=5, column=0)
s14.grid(row=5, column=1)
s15.grid(row=5, column=2)
s16.grid(row=5, column=3)

s17.grid(row=6, column=0)
s18.grid(row=6, column=1)
s19.grid(row=6, column=2)
s20.grid(row=6, column=3)

s25.grid(row=7, column=1)
bullseye.grid(row=7, column=2)

root.mainloop()
