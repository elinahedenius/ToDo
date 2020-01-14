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

        print('These are your available lists: ')
        for x in listOfLists:
            print(x.name)
        newTaskList = input('Which one do you want to put your new task in? (type none for none): ')
        for x in listOfLists:
            if newTaskList in x.name:
                x.append(newTask)
            elif newTaskList not in x.name:
                createNewList = input('That is not a list. Do you want to create it? (y/n)')
                if createNewList == 'y':
                    newListList = ('Put into this list as a sublist (type none for none): ')
                    lists.makeNewFromScratch(newTaskList, newListList)
                    print('You have sucessfully added ' + newTaskName + ' to the list ' + newTaskList + '.')
                elif createNewList == 'n':
                    print('ok!')
                    continue

        newTask = tasks(newTaskName, newTaskDate, newTaskList)
        listOfTasks.append(newTask)


class lists():
    def __init__(list, name, listToBeIn):
        list.name = name
        list.list = listToBeIn

    def makeNew():
        newListName = input('List name: ')
        newListList = input('Put into this list as a sublist (type none for none): ')

        newList = list()
        newList = lists(newListName, newListList)

        listOfLists.append(newList)


while True:
    choice = input('What do you want to do (create new task -> ct, create new list -> cl)')

    if choice == 'ct':
        tasks.makeNew()

    elif choice == 'cl':
        lists.makeNew()
