# for python 2.7
from Tkinter import *
import ScrolledText
import tkFileDialog, tkMessageBox, tkSimpleDialog

# Root for main window
root = Tk(className = ' TEXT EDITOR')
TextArea = ScrolledText.ScrolledText(root, width=200, height=80)

# Functions for Menu

# Create new file
def newFile():
    # If there is content in existing file
    if len(TextArea.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno("Save?", "You have unsaved changes. Do you want to save?"):
            saveFile()
        else:
            TextArea.delete('1.0', END)
    root.title("TEXT EDITOR")

# Open File
def openFile():
    file = tkFileDialog.askopenfile(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

    if file != None:
        contents = file.read()
        TextArea.insert('1.0', contents)
        file.close()

# Save File
def saveFile():
    file = tkFileDialog.asksaveasfile(mode='w')

    if file != None:
        # slice off the last character from get, as an extra return (enter) is added
        data = TextArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()

# About
def aboutNotpad():
    tkMessageBox.showinfo("About", "A Python alternative to NotePad!!!")

# To exit from notepad
def exitRoot():
    if tkMessageBox.askyesno("quit", "Are you sure you want to quit?"):
        root.destroy()

# To find string in file
def findInFile():
    findString = tkSimpleDialog.askstring("Find....", "Enter Text")
    textData = TextArea.get('1.0', END)

    occurances = textData.upper().count(findString.upper())

    if occurances > 0:
        label = tkMessageBox.showinfo("Results", findString +' '+ "has"+' '+ str(occurances)+' '+"occurances.")
    else:
        label = tkMessageBox.showinfo("Results", "No record found")

# Menu Option
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New File", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Find", command=findInFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitRoot)

helpMenu = Menu(menu)
menu.add_command(label="About", command=aboutNotpad)

TextArea.pack()
# To keep window Open
root.mainloop()
