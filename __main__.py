#from kivy.app import App
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.label import Label
#from kivy.uix.textinput import TextInput
import requests

listOfTasks = []
listOfLists = []
listOfParentLists = []

listCount = 0

class Tasks():

    def __init__(self, name, due):
        self.name = name
        self.due = due

    def __str__(self):
        return self.name + "ska vara klart" + self.due

def makeNewTask():
    newTaskName = input('Task name: ')
    newTaskDate = input('Task due date: ')

    newTask = Tasks(newTaskName, newTaskDate)
    listOfTasks.append(newTask)

    print('These are your available lists: ')
    for x in listOfLists:
        print(x[0])
    newTaskList = input('Which one do you want to put your new task in? (type none for none): ')
    if newTaskList == 'none':
        return;
    else:
        for x in listOfLists:
            x.append(newTask)

class List(list ):
    def __init__(self, name):
        self.name = name

def makeNewList():
    global listCount
    name = input('Name of new list: ')
    newList = List(name)
    parentList = input('Put this list into this list (type none for none): ')
    if parentList == 'none':
        listOfParentLists.append(newList)
    elif parentList != 'none':
        for x in listOfLists:
            if x.name == parentList:
                x.append(newList)
    newList.append(name)
    listOfLists.append(newList)
    listCount = listCount + 1
    return newList

while True:
    print('These are your current lists: ')
    for x in listOfParentLists:
        print(x.name + ':')
        for a in x:
            if a == x.name:
                continue
            else:
                print('     ' + a.name)

    choice = input('What do you want to do? (see "help" for options) ')

    if choice == 'ct':
        makeNewTask()

    elif choice == 'cl':
        makeNewList()

    elif choice == 'exit':
        break

    elif choice == 'help':
        print (' cl → create new list \n ct → create new task \n exit → exit program')

    else:
        print('that is not a valid command :/')
