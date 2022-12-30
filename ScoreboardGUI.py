from tkinter import * 

root = Tk() 

p1 = Label(root, text="Player 1", font=(25)) 
p2 = Label(root, text="Player 2", font=(25))
p1ScoreLabel = Label(root, text=301, font=(25))
p2ScoreLabel = Label(root, text=301, font=(25))

p1Score = 301
p2Score = 301 

# function for calculating player's dart score
def calculateScore(segmentValue):
    print("hello world")

# Create buttons for dartboard segments

d = Button(text="double")
t = Button(text="triple")

s1 = Button(text="1", command=lambda: calculateScore(1))
s2 = Button(text="2", command=lambda: calculateScore(2))
s3 = Button(text="3", command=lambda: calculateScore(3))
s4 = Button(text="4", command=lambda: calculateScore(4))
s5 = Button(text="5", command=lambda: calculateScore(5))
s6 = Button(text="6", command=lambda: calculateScore(6))
s7 = Button(text="7", command=lambda: calculateScore(7))
s8 = Button(text="8", command=lambda: calculateScore(8))
s9 = Button(text="9", command=lambda: calculateScore(9))
s10 = Button(text="10", command=lambda: calculateScore(10))
s11 = Button(text="11", command=lambda: calculateScore(11))
s12 = Button(text="12", command=lambda: calculateScore(12))
s13 = Button(text="13", command=lambda: calculateScore(13))
s14 = Button(text="14", command=lambda: calculateScore(14))
s15 = Button(text="15", command=lambda: calculateScore(15))
s16 = Button(text="16", command=lambda: calculateScore(16))
s17 = Button(text="17", command=lambda: calculateScore(17))
s18 = Button(text="18", command=lambda: calculateScore(18))
s19 = Button(text="19", command=lambda: calculateScore(19))
s20 = Button(text="20", command=lambda: calculateScore(20))
s25 = Button(text="25 Ring", command=lambda: calculateScore(25))
bullseye = Button(text="Bullseye", command=lambda: calculateScore(50)) 

# Organizing Labels, Buttons, and Frames on root using grid()

p1.grid(row=0, column=4)
p2.grid(row=0, column=5) 

d.grid(row=1, column=1)
t.grid(row=1,column=2)

p1ScoreLabel.grid(row=1, column=4)
p2ScoreLabel.grid(row=1, column=5)

s1.grid(row=2, column=0)
s2.grid(row=2, column=1)
s3.grid(row=2,column=2)
s4.grid(row=2,column=3)

s5.grid(row=3, column=0)
s6.grid(row=3, column=1)
s7.grid(row=3,column=2)
s8.grid(row=3,column=3)

s9.grid(row=4, column=0)
s10.grid(row=4, column=1)
s11.grid(row=4,column=2)
s12.grid(row=4,column=3)

s13.grid(row=5, column=0)
s14.grid(row=5, column=1)
s15.grid(row=5,column=2)
s16.grid(row=5,column=3)

s17.grid(row=6, column=0)
s18.grid(row=6, column=1)
s19.grid(row=6,column=2)
s20.grid(row=6,column=3)

s25.grid(row=7, column=1)
bullseye.grid(row=7, column=2)

root.mainloop()