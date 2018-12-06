from tkinter import *

import pkgutil
import re

from src.util import ALL_STRATEGIES

import src.run_demo_simulation as run_demo
import src.run_simulations_with_results as run_sim

import datasets.scenarios as scenarios

ANY_DENSITY = "any"

scenarios_list = []
datasets_map   = {}
densities_map   = {}

prefix = scenarios.__name__ + "."
for importer, module_name, ispkg in pkgutil.iter_modules(scenarios.__path__,
                                                         prefix):
    scenarios_list.append(module_name)

    scenario_code = re.match(".*([0-9]+x[0-9]+_[0-9]+).*", module_name).group(1)
    datasets_name = "datasets.datasets_{}".format(scenario_code)
    datasets = __import__(datasets_name, fromlist="dummy")

    datasets_list = []
    densities = set()
    d_prefix = datasets.__name__ + "."
    for d_importer, d_module_name, d_ispkg in pkgutil.iter_modules(
                                                  datasets.__path__, d_prefix):
        datasets_list.append(d_module_name)

        traffic_density = re.match(".*dataset_[0-9]+x[0-9]+_[0-9]+_([0-9]+).*",
                                   d_module_name).group(1)
        densities.add(traffic_density)

    densities_map[module_name] = [ANY_DENSITY] + sorted(densities)

    datasets_map[module_name] = datasets_list

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
               command=lambda: frame.tkraise()).pack(padx=5, pady=5)

# main menu
mainFrame = MyFrame(window, "Main Menu")

# run simulation
simFrame     = MyFrame(window, "Run Simulation")
demoFrame    = MyFrame(window, "Run Demo Simulation")
fullSimFrame = MyFrame(window, "Run Simulation with Results")

# data generation
sceneFrame = MyFrame(window, "Generate Test Scenario")
dataFrame  = MyFrame(window, "Generate Test Data")

# analyse results
analyseFrame = MyFrame(window, "Analyse Simulation Results")

#############
# main menu #
#############

mainFrame.createButton(dataFrame)
mainFrame.createButton(simFrame)
mainFrame.createButton(analyseFrame)

######################
# generate test data #
######################

dataFrame.createButton(sceneFrame)
dataFrame.createReturnButton(mainFrame)

##########################
# generate test scenario #
##########################

sceneFrame.createReturnButton(dataFrame)

##################
# run simulation #
##################

simFrame.createButton(demoFrame)
simFrame.createButton(fullSimFrame)

#######################
# run demo simulation #
#######################

def changeScenario(event):
    items = demoSceneBox.curselection()
    if not items:
        return
    scenario = demoSceneBox.get(items[0])

    menu = densityDropdown["menu"]
    menu.delete(0, END)
    for density in densities_map[scenario]:
        menu.add_command(label=density,
                         command=lambda value=density: changeDensity(value))
    densityVar.set(ANY_DENSITY)

    demoDataBox.delete(0, END)
    for module in datasets_map[scenario]:
        demoDataBox.insert(END, module)

    #if demoDataBox.size():
    #    demoDataBox.config(width=0)
    #else:
    #    demoDataBox.config(width=20)

def changeDensity(density):
    densityVar.set(density)

    items = demoSceneBox.curselection()
    if not items:
        return
    scenario = demoSceneBox.get(items[0])

    demoDataBox.delete(0, END)
    if density == ANY_DENSITY:
        for module in datasets_map[scenario]:
            demoDataBox.insert(END, module)
    else:
        pattern = re.compile("dataset_[0-9]+x[0-9]+_[0-9]+_{}".format(density))

        for module in datasets_map[scenario]:
            if pattern.search(module):
                demoDataBox.insert(END, module)

    #if demoDataBox.size():
    #    demoDataBox.config(width=0)
    #else:
    #    demoDataBox.config(width=20)

def startDemo():
    items = demoStratBox.curselection()
    if not items:
        return
    strategy = strategyMap[demoStratBox.get(items[0])]

    items = demoSceneBox.curselection()
    if not items:
        return
    scenario = demoSceneBox.get(items[0])

    items = demoDataBox.curselection()
    if not items:
        return
    dataset = demoDataBox.get(items[0])

    window.destroy()
    run_demo.run(scenario, dataset, strategy)

# container frame for grid alignment
demoGridFrame = Frame(demoFrame)

# box for selecting scenario
demoSceneFrame = Frame(demoGridFrame)
Label(demoSceneFrame,
      text="Choose Scenario\nFormat: columns, rows, block size").pack()

demoSceneScrollbar = Scrollbar(demoSceneFrame)
demoSceneScrollbar.pack(side=RIGHT, fill=Y)

demoSceneBox = Listbox(demoSceneFrame, selectmode=SINGLE, exportselection=0,
                       yscrollcommand=demoSceneScrollbar.set)
demoSceneBox.bind('<<ListboxSelect>>', changeScenario)
demoSceneBox.pack()

demoSceneScrollbar.config(command=demoSceneBox.yview)
demoSceneFrame.grid(column=0, row=0)

for module in scenarios_list:
    demoSceneBox.insert(END, module)

if demoSceneBox.size():
    demoSceneBox.config(width=0)

# dropdown menu for specifying traffic density
demoDenseFrame = Frame(demoGridFrame, bd=2)
Label(demoDenseFrame, text="Filter by Traffic Density\n(cars per minute)").pack()

densityVar = StringVar()
densityVar.set(ANY_DENSITY)

densityDropdown = OptionMenu(demoDenseFrame, densityVar, ANY_DENSITY)
densityDropdown.pack()

demoDenseFrame.grid(column=1, row=0)

# listbox for selecting dataset
demoDataFrame = Frame(demoGridFrame)
Label(demoDataFrame, text="Choose Dataset\nFormat: scenario code, traffic density, turn bias, trial id").pack()

demoDataScrollbar = Scrollbar(demoDataFrame)
demoDataScrollbar.pack(side=RIGHT, fill=Y)

demoDataBox = Listbox(demoDataFrame, selectmode=SINGLE, exportselection=0,
                       yscrollcommand=demoDataScrollbar.set)
demoDataBox.pack()
demoDataBox.config(width=50)

demoDataScrollbar.config(command=demoDataBox.yview)
demoDataFrame.grid(column=0, row=1, columnspan=2)

# listbox for selecting strategy
demoStratFrame = Frame(demoGridFrame)
Label(demoStratFrame, text="Choose Strategy").pack()

strategyMap = {}

demoStratScrollbar = Scrollbar(demoStratFrame)
demoStratScrollbar.pack(side=RIGHT, fill=Y)

demoStratBox = Listbox(demoStratFrame, selectmode=SINGLE, exportselection=0,
                       yscrollcommand=demoStratScrollbar.set)
demoStratBox.pack()
demoStratBox.config(width=0)

demoStratScrollbar.config(command=demoStratBox.yview)
demoStratFrame.grid(column=0, row=2)

for strategy, description in ALL_STRATEGIES:
    strategyMap[description] = strategy
    demoStratBox.insert(END, description)

Button(demoGridFrame, text="Start Demo",
       command=startDemo).grid(column=1, row=2)

demoGridFrame.pack()

demoFrame.createReturnButton(mainFrame)

###############################
# run simulation with results #
###############################

fullSimFrame.createReturnButton(mainFrame)

##############################
# analyse simulation results #
##############################

analyseFrame.createReturnButton(mainFrame)

#############
# start gui #
#############

mainFrame.tkraise()
window.mainloop()

