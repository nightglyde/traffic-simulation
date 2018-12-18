from tkinter import *

import math
import pkgutil
import re

from src.util import ALL_STRATEGIES

import src.generate_test_data.generate_datasets as gen_data
import src.generate_test_data.generate_scenario as gen_scene
import src.run_demo_simulation as run_demo
import src.run_simulations_with_results as run_sim

import datasets.scenarios as scenarios

CHOOSE_SCENARIO_TEXT = '''Choose Scenario
...scenario_COLSxROWS_BlockSize'''

CHOOSE_DATASET_TEXT = '''Choose Dataset
...COLSxROWS_BlockSize_TrafficDensity_TurnBias_TrialNum'''

DEFAULT_DATA_TEXT = '''How proposed changes will affect dataset numbers:
\t\t[Existing + New = Total]'''

DEFAULT_SCENE_TEXT = "Generate a scenario with these dimensions:"

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
        return Button(frame, text=self.description,
                      command=lambda: self.tkraise())

    def createReturnButton(self, frame):
        return Button(frame, text="Return to {}".format(self.description),
                      command=lambda: self.tkraise())

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

dataFrame.createButton(mainFrame).pack()
simFrame.createButton(mainFrame).pack()
analyseFrame.createButton(mainFrame).pack()

######################
# generate test data #
######################

def getDataParameters():
    items = dataSceneBox.curselection()
    if not items:
        return False
    scenario = dataSceneBox.get(items[0])

    try:
        numTrials = int(numTrialsEntry.get())
        if numTrials < 1:
            return False

        minDensity = int(minDensityEntry.get())
        if minDensity < 10:
            minDensity = 10
        else:
            minDensity = int(math.ceil(minDensity / 10.0)) * 10

        maxDensity = int(maxDensityEntry.get())
        maxDensity = int(math.floor(maxDensity / 10.0)) * 10

        if maxDensity < minDensity:
            return False

    except ValueError:
        return False

    m = re.match(".*([0-9]+x[0-9]+_[0-9]+).*", scenario)
    if m:
        scenario_code = m.group(1)
    else:
        return False

    return scenario, scenario_code, numTrials, minDensity, maxDensity

def validateDataFields(*args):
    parameters = getDataParameters()
    if not parameters:
        dataMessage.config(text=DEFAULT_DATA_TEXT)
        return

    scenario, scenario_code, numTrials, minDensity, maxDensity = parameters

    countMap = {}
    for density in densities_map[scenario]:
        try:
            densityInt = int(density)
        except ValueError:
            continue

        if not minDensity <= densityInt <= maxDensity:
            continue

        pattern = re.compile("dataset_[0-9]+x[0-9]+_[0-9]+_{}".format(density))

        testCaseCount = 0
        for module in datasets_map[scenario]:
            if pattern.search(module):
                testCaseCount += 1

        countMap[densityInt] = testCaseCount

    message = [DEFAULT_DATA_TEXT]

    for density in range(minDensity, maxDensity+1, 10):
        if density in countMap:
            testCaseCount = countMap[density]
        else:
            testCaseCount = 0

        message.append("    density={}:\t    {} + {} = {}".format(
            density, testCaseCount, numTrials, testCaseCount + numTrials))

    dataMessage.config(text="\n".join(message))

def startGeneratingData():
    parameters = getDataParameters()
    if not parameters:
        return

    window.destroy()
    gen_data.run(*parameters)

# container frame for grid alignment
dataGridFrame = Frame(dataFrame)

# box for selecting scenario
dataSceneFrame = Frame(dataGridFrame)
Label(dataSceneFrame, text=CHOOSE_SCENARIO_TEXT).pack()

dataSceneScrollbar = Scrollbar(dataSceneFrame)
dataSceneScrollbar.pack(side=RIGHT, fill=Y)

dataSceneBox = Listbox(dataSceneFrame, selectmode=SINGLE, exportselection=0,
                       yscrollcommand=dataSceneScrollbar.set)
dataSceneBox.bind('<<ListboxSelect>>', validateDataFields)
dataSceneBox.pack()

dataSceneScrollbar.config(command=dataSceneBox.yview)
dataSceneFrame.grid(column=0, row=0)#, columnspan=2)

for module in scenarios_list:
    dataSceneBox.insert(END, module)

if dataSceneBox.size():
    dataSceneBox.config(width=0)

# button to go to generate test scenario screen
dataGenSceneFrame = Frame(dataGridFrame)

Label(dataGenSceneFrame, text='''If the list doesn't have the scenario
you want, click this button:''').pack()

sceneFrame.createButton(dataGenSceneFrame).pack()

dataGenSceneFrame.grid(column=1, row=0)

# box for choosing test case parameters
dataFieldsFrame = Frame(dataGridFrame)

# box for choosing number of trials
dataTrialsFrame = Frame(dataFieldsFrame)

Label(dataTrialsFrame, text="Number of Trials").pack()

numTrialsEntry = Entry(dataTrialsFrame, width=5, justify=CENTER)
numTrialsEntry.bind("<KeyRelease>", validateDataFields)
numTrialsEntry.insert(0, 1)
numTrialsEntry.pack()

dataTrialsFrame.grid(column=0, row=0)

# box for choosing traffic density
dataDenseFrame = Frame(dataFieldsFrame)

Label(dataDenseFrame, text="Traffic Density").grid(
    column=0, row=0, columnspan=2)

Label(dataDenseFrame, text="Minimum:").grid(column=0, row=1)

minDensityEntry = Entry(dataDenseFrame, width=5, justify=CENTER)
minDensityEntry.bind("<KeyRelease>", validateDataFields)
minDensityEntry.insert(0, 10)
minDensityEntry.grid(column=1, row=1)

Label(dataDenseFrame, text="Maximum:").grid(column=0, row=2)

maxDensityEntry = Entry(dataDenseFrame, width=5, justify=CENTER)
maxDensityEntry.bind("<KeyRelease>", validateDataFields)
maxDensityEntry.insert(0, 150)
maxDensityEntry.grid(column=1, row=2)

dataDenseFrame.grid(column=1, row=0)

dataFieldsFrame.grid(column=0, row=1, columnspan=2)

# text box to display info about data that will be generated
dataMessage = Label(dataGridFrame, bd=5, justify=LEFT)
dataMessage.grid(column=0, row=2)
validateDataFields()

# button to start generating data
Button(dataGridFrame, text="Start Generating Data",
       command=startGeneratingData).grid(column=1, row=2)

dataGridFrame.pack()

mainFrame.createReturnButton(dataFrame).pack(padx=5, pady=5)

##########################
# generate test scenario #
##########################

def getSceneParameters():
    try:
        num_cols = int(columnsEntry.get())
        if num_cols < 0:
            num_cols = 0

        num_rows = int(rowsEntry.get())
        if num_rows < 0:
            num_rows = 0

        block_size = int(blockSizeEntry.get())
        if block_size < gen_scene.MIN_BLOCK_SIZE:
            block_size = gen_scene.MIN_BLOCK_SIZE

    except ValueError:
        return False

    return num_cols, num_rows, block_size

def validateSceneFields(*args):
    parameters = getSceneParameters()
    if not parameters:
        sceneMessage.config(text=DEFAULT_SCENE_TEXT+"\n\tInvalid parameters!")
        return

    num_cols, num_rows, block_size = parameters

    message = [DEFAULT_SCENE_TEXT,
        "    num_cols: {}".format(num_cols),
        "    num_rows: {}".format(num_rows),
        "    block_size: {}".format(block_size),
    ]

    pattern = re.compile(".*scenario_{}x{}_{}.*".format(
        num_cols, num_rows, block_size))

    for scenario in scenarios_list:
        if pattern.match(scenario):
            message.append("\nThis scenario already exists!\nIf you try to generate it again,\nnothing will happen.")
            break

    sceneMessage.config(text="\n".join(message))

def startGeneratingScene():
    parameters = getSceneParameters()
    if not parameters:
        return

    window.destroy()
    gen_scene.run(*parameters)

# container frame for grid alignment
sceneGridFrame = Frame(sceneFrame)

# box for choosing number of blocks (rows and columns)
sceneBlocksFrame = Frame(sceneGridFrame)

Label(sceneBlocksFrame, text="Number of Blocks").grid(
    column=0, row=0, columnspan=2)

Label(sceneBlocksFrame, text="Columns:").grid(column=0, row=1)

columnsEntry = Entry(sceneBlocksFrame, width=5, justify=CENTER)
columnsEntry.bind("<KeyRelease>", validateSceneFields)
columnsEntry.insert(0, 1)
columnsEntry.grid(column=1, row=1)

Label(sceneBlocksFrame, text="Rows:").grid(column=0, row=2)

rowsEntry = Entry(sceneBlocksFrame, width=5, justify=CENTER)
rowsEntry.bind("<KeyRelease>", validateSceneFields)
rowsEntry.insert(0, 1)
rowsEntry.grid(column=1, row=2)

sceneBlocksFrame.grid(column=0, row=0)

# box for choosing size of blocks
sceneBlockSizeFrame = Frame(sceneGridFrame)

Label(sceneBlockSizeFrame, text="Size of Blocks").pack()

blockSizeEntry = Entry(sceneBlockSizeFrame, width=5, justify=CENTER)
blockSizeEntry.bind("<KeyRelease>", validateSceneFields)
blockSizeEntry.insert(0, 50)
blockSizeEntry.pack()

sceneBlockSizeFrame.grid(column=1, row=0)

# text box to display info about scene that will be generated
sceneMessage = Label(sceneGridFrame, bd=5, justify=LEFT)
sceneMessage.grid(column=0, row=1)
validateSceneFields()

# button to start generating scene
Button(sceneGridFrame, text="Start Generating Scenario",
       command=startGeneratingScene).grid(column=1, row=1)

sceneGridFrame.pack()

dataFrame.createReturnButton(sceneFrame).pack(padx=5, pady=5)

##################
# run simulation #
##################

demoFrame.createButton(simFrame).pack()
fullSimFrame.createButton(simFrame).pack()

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
Label(demoSceneFrame, text=CHOOSE_SCENARIO_TEXT).pack()

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
Label(demoDenseFrame, text="Filter Dataset by Traffic Density\n(cars per minute)").pack()

densityVar = StringVar()
densityVar.set(ANY_DENSITY)

densityDropdown = OptionMenu(demoDenseFrame, densityVar, ANY_DENSITY)
densityDropdown.pack()

demoDenseFrame.grid(column=1, row=0)

# listbox for selecting dataset
demoDataFrame = Frame(demoGridFrame)
Label(demoDataFrame, text=CHOOSE_DATASET_TEXT).pack()

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

demoStratScrollbar = Scrollbar(demoStratFrame)
demoStratScrollbar.pack(side=RIGHT, fill=Y)

demoStratBox = Listbox(demoStratFrame, selectmode=SINGLE, exportselection=0,
                       yscrollcommand=demoStratScrollbar.set)
demoStratBox.pack()
demoStratBox.config(width=0)

demoStratScrollbar.config(command=demoStratBox.yview)
demoStratFrame.grid(column=0, row=2)

strategyMap = {}
for strategy, description in ALL_STRATEGIES:
    strategyMap[description] = strategy
    demoStratBox.insert(END, description)

# button to start the demo
Button(demoGridFrame, text="Start Demo",
       command=startDemo).grid(column=1, row=2)

demoGridFrame.pack()

mainFrame.createReturnButton(demoFrame).pack(padx=5, pady=5)

###############################
# run simulation with results #
###############################

mainFrame.createReturnButton(fullSimFrame).pack(padx=5, pady=5)

##############################
# analyse simulation results #
##############################

mainFrame.createReturnButton(analyseFrame).pack(padx=5, pady=5)

#############
# start gui #
#############

mainFrame.tkraise()
window.mainloop()

