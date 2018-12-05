from tkinter import *

from src.util import *

import src.run_demo_simulation as run_demo
import src.run_simulations_with_results as run_sim

window = Tk()

class MyFrame(Frame):
    def __init__(self, parent=None, description=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.parent      = parent
        self.description = description

        self.grid(row=0, column=0, sticky="news")

    def tkraise(self, *args, **kwargs):
        Frame.tkraise(self, *args, **kwargs)

        self.parent.title(self.description)

    def createButton(self, frame):
        Button(self, text=frame.description,
               command=lambda: frame.tkraise()).pack()

    def createReturnButton(self, frame):
        Button(self, text="Return to {}".format(frame.description),
               command=lambda: frame.tkraise()).pack()

# main menu
mainFrame = MyFrame(window, "Main Menu")

# run simulation
demoFrame  = MyFrame(window, "Run Demo Simulation")
simFrame   = MyFrame(window, "Run Simulation with Results")

# data generation
sceneFrame = MyFrame(window, "Generate Test Scenario")
dataFrame  = MyFrame(window, "Generate Test Data")

# analyse results
analyseFrame = MyFrame(window, "Analyse Simulation Results")

#############
# main menu #
#############

mainFrame.createButton(demoFrame)
mainFrame.createButton(simFrame)
mainFrame.createButton(sceneFrame)
mainFrame.createButton(dataFrame)
mainFrame.createButton(analyseFrame)

#######################
# run demo simulation #
#######################

listbox = Listbox(demoFrame, selectmode=SINGLE)
listbox.pack()

strategyMap = {}
for strategy, description in ALL_STRATEGIES:
    strategyMap[description] = strategy
    listbox.insert(END, description)

def startDemo(listbox, strategyMap):
    items = listbox.curselection()
    if not items:
        return

    strategy = strategyMap[listbox.get(items[0])]

    window.destroy()
    run_demo.run(strategy)

Button(demoFrame, text="Start Demo",
       command=lambda: startDemo(listbox, strategyMap)).pack()

demoFrame.createReturnButton(mainFrame)

###############################
# run simulation with results #
###############################

simFrame.createReturnButton(mainFrame)

##########################
# generate test scenario #
##########################

sceneFrame.createReturnButton(mainFrame)

######################
# generate test data #
######################

dataFrame.createReturnButton(mainFrame)

##############################
# analyse simulation results #
##############################

analyseFrame.createReturnButton(mainFrame)

#############
# start gui #
#############

mainFrame.tkraise()
window.mainloop()

