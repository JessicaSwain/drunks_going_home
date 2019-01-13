# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#-----------------------------------IMPORTS----------------------------------#
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot as plot
import DRUNKCHECKFRAMEWORK as ownclass
import csv
import matplotlib.animation
import matplotlib.backends.backend_tkagg
#-------------------------------VARIABLE SET UP------------------------------#
num_of_drunks = 25
num_of_iterations = 100
neighbourhood = 20

'''below is a test to ensure the .txt file writing works'''
#testing = 563056
#test = open('writingtotexttest.txt','w') 
#test.write("testing to see if this works" + "\n") 
#test.write(str(testing)) 
#test.close()
#------------------------------------LISTS-----------------------------------#
environment = []
#empty environment list which the .txt file will be imported into
drunks = []
#where all functions and the class 'DRUNKCHECKFRAMEWORK' is linking to
distances = []

DrunkNumbering = {"drunk1": 10, "drunk2": 20, "drunk3": 30, "drunk4": 40, "drunk5": 50, "drunk6": 60, "drunk7": 70, "drunk8": 80, "drunk9": 90, "drunk10": 100, "drunk11": 110, "drunk12": 120, "drunk13": 130, "drunk14": 140, "drunk15": 150, "drunk16": 160, "drunk17": 170, "drunk18": 180, "drunk19": 190, "drunk20": 200, "drunk21": 210, "drunk22": 220, "drunk23": 230, "drunk24": 240, "drunk25": 250}
drunknum = str([DrunkNumbering.values()])
#-----------------------IMPORTING IN THE ENVIRONMENT ------------------------#
f = open('drunkplan.txt', 'r')
#r is for read only
reader = csv.reader (f)
for row in reader:
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(int(value))

#now the environment has the numbers seen in the text file

f.close()
#----------------------------PLOTTING ENVIRONMENT----------------------------#
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)
#----------------------------SETTING UP DRUNKS-------------------------------#
position = 0

for i in range(num_of_drunks):
    position += 10

    y = 0
    x = 0
    
    '''CODE CHECK'''
    print("drunk number assignment",position)
    
    drunks.append(ownclass.Drunk(environment, drunks, position, y, x))
    
results = open('drunkresults.txt','w') 
results.write(str(position) + "\n")  
results.close()
#---------------------------FUNCTIONS AND ANIMATION--------------------------#
carry_on = True

def update(frame_number):
    
    fig.clear()  
    
    plot.xlim(0, 300)
    plot.ylim(0, 300)
    plot.imshow(environment)
    
    global carry_on   

    for i in range(num_of_drunks):
        drunks[i].move()
        print('------------------------------------------------')
        drunks[i].eat()
 #       drunks[i].share_with_neighbours(neighbourhood)
        
    
    for i in range(num_of_drunks):
        plot.scatter(drunks[i]._x, drunks[i]._y)

		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10000) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1  

results = open('drunkresults.txt','a') 
results.write(str(y) + "\n")  
results.write(str(x) + "\n")
results.close()         
#--------------------------------------ANIMATION-----------------------------#
def run():
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

#matplotlib.pyplot.show()
    '''taken the above out and put canvas.show() in instead'''
#--------------------------------POP UP WINDOW-------------------------------#
root = tkinter.Tk() 
root.wm_title("Drunks Getting Home")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#root = tkinter.Tk() 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="model menu", menu=model_menu)
model_menu.add_command(label="run model", command=run)
#----------------------------------------------------------------------------#

tkinter.mainloop()
