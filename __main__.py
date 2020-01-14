from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

listOfTasks = []
listOfLists = []

class tasks():

    def __init__(task, name, due, list):
        task.name = name
        task.due = due
        task.list = list

    def makeNew():
        newTaskName = input('Task name: ')
        newTaskDate = input('Task due date: ')
        newTaskList = input('Put into this list (type none for none): ')

        newTask = tasks(newTaskName, newTaskDate, newTaskList)
        listOfTasks.append(newTask)
        print(listOfTasks)

while True:
    choice = input('What do you want to do (create new task -> ct, create new list = cl)')

    if choice == 'ct':
        tasks.makeNew()

    elif choice == 'cl':
        continue
