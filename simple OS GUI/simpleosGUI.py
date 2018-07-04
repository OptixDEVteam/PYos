from tkinter import *
from tkinter import ttk

root = Tk()
# rootG = Tk()
root.option_add("*TearOff", False)
menubar = Menu(root)

import pickle
import time
import random
import math
import os.path
import os
import threading
import inspect
import hashlib
"""
cipherfolderI = PhotoImage(file = "/Users/carsonott/Google Drive/python/simple OS GUI/Cryptography-512.gif")
gamefolderI = PhotoImage(file = "/Users/carsonott/Google Drive/python/simple OS GUI/Play-Games-icon.gif")
dicegameI = PhotoImage(file = "/Users/carsonott/Google Drive/python/simple OS GUI/board-games-icon--15.gif")
calcI = PhotoImage(file = "/Users/carsonott/Google Drive/python/simple OS GUI/imgres.gif")
textI = PhotoImage(file = "/Users/carsonott/Google Drive/python/simple OS GUI/12.gif")
fileI = PhotoImage(file = "/Users/carsonott/Google Drive/python/simple OS GUI/folder-icon-512x512.gif")
ciphershiftI = PhotoImage(file = "/Users/carsonott/Google Drive/python/simple OS GUI/shift-384.gif")
cipheralphI = PhotoImage(file = "/Users/carsonott/Google Drive/python/simple OS GUI/alphabet-uppercase-letter-a-512.gif")
"""

status = False
# Variables
AdminS = False
Path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(Path)


if os.path.exists(Path+"/usedbefore.p") == False:
    pickle.dump("True", open( "usedbefore.p", "wb" ) )
    pickle.dump(["_", "-"], open( "docNames.p", "wb" ) )


# Definitions of Objects
v = IntVar()
program = StringVar()
programbox = ttk.Combobox(root)
startprogram = ttk.Button(root)
symSense = StringVar()
num1 = StringVar()
num2 = StringVar()
evaluate = ttk.Button(root)
box1 = ttk.Entry(root)
box2 = ttk.Entry(root)
sym = ttk.Combobox(root)
goforward = ttk.Button(root)
answer = ttk.Label(root)
filelabel = ttk.Label(root)
filename = ttk.Entry(root)
Text = Text(root)
TeditSave = ttk.Button(root)
TeditExit = ttk.Button(root)
filesystem = ttk.Treeview(root)
fileOpen = ttk.Button(root)
fileExit = ttk.Button(root)
fileDelete = ttk.Button(root)
AdminEntry = ttk.Entry(root)
AdminSubmit = ttk.Button(root)

# Functions
def forgetA():
    labelPass.pack_forget()
    password.pack_forget()
    username.pack_forget()
    clear.pack_forget()
    submit.pack_forget()
    signup.pack_forget()
    programF()
    labelUser.pack_forget()
    AdminEntry.pack_forget()
    AdminSubmit.pack_forget()
    filesystem.pack_forget()
    fileOpen.pack_forget()
    fileExit.pack_forget()
    fileDelete.pack_forget()
    filelabel.pack_forget()
    filename.pack_forget()
    Text.pack_forget()
    TeditSave.pack_forget()
    TeditExit.pack_forget()
    goforward.pack_forget()
    answer.pack_forget()
    box1.pack_forget()
    sym.pack_forget()
    box2.pack_forget()
    evaluate.pack_forget()
def clearentry():
    username.delete(0, END)
    password.delete(0, END)
    labelUser.config(foreground = "black", text = "Username:")
    labelPass.config(foreground = "black", text = "Password:")

def setup():
    root.config(menu = menubar)
    file = Menu(menubar)
    menu_ = Menu(menubar)
    menubar.add_cascade(menu = file, label = "File")
    menubar.add_cascade(menu = menu_, label = "Menu")
    file.add_command(label = "New", command = textedit)
    file.add_command(label = "Open", command = fileexplorer)
    menu_.add_command(label = "Menu", command = programlist)
#    menu_.add_seperator()
    menu_.add_command(label = "Calculator", command = calc)
    menu_.add_command(label = "Games", command = games)
    
def submitentry():
    if v.get() == 1:
        pickle.dump( hashlib.sha1(bytes(username.get(), 'utf-8')).hexdigest(), open( "Username.p", "wb" ) )
        pickle.dump( hashlib.sha1(bytes(password.get(), 'utf-8')).hexdigest(), open( "Password.p", "wb" ) )
        labelUser.config(text = "Username: created")
        labelPass.config(text = "Password: created")
    elif v.get() == 0 and signin() == True:
        status = True
        labelUser.config(foreground = "green", text = "SIGN IN SUCCESFUL")
        labelPass.pack_forget()
        password.pack_forget()
        username.pack_forget()
        clear.pack_forget()
        submit.pack_forget()
        signup.pack_forget()
        setup()
        programlist()
        time.sleep(1)
def programlist():
    forgetA()
    labelUser.config(foreground = "black", text = "Program List")
    programbox.config(textvariable = program, value = ("Calculator","Text Editor","File Explorer","Games","Other Programs","Sign Out",))
    labelUser.pack()
    programbox.pack()
    startprogram.config(text = "Start Program", command = programstart)
    startprogram.pack()
def programstart():    
    if program.get() == "Calculator":
        calc()
    elif program.get() == "Text Editor":
        textedit()
    elif program.get() == "File Explorer":
        fileexplorer()
    elif program.get() == "Games":
        games()
    elif program.get() == "Other Programs":
        other()
    elif program.get() == "Sign Out":
        signinbox()
    elif program.get() == "ADMIN":
        AdminSignup()
    else:
        print("program not found")
        programlist()
def programF():
    labelUser.pack_forget()
    programbox.pack_forget()
    startprogram.pack_forget()
def AdminSignup():
    forgetA()
    if os.path.exists(Path+"/AdminCode.p") == False:
        print
        labelUser.config(text = "Admin Signup")
        AdminEntry.config(width = 30)
        AdminSubmit.config(text = "Submit", command = SubmitAdmin)
        labelUser.pack()
        AdminEntry.pack()
        AdminSubmit.pack()
    else:
        labelUser.config(text = "Admin Signin")
        AdminEntry.config(width = 30)
        AdminSubmit.config(text = "Submit", command = SigninAdmin)
        labelUser.pack()
        AdminEntry.pack()
        AdminSubmit.pack()
def SubmitAdmin():
    labelUser.pack_forget()
    AdminEntry.pack_forget()
    AdminSubmit.pack_forget()
    pickle.dump(hashlib.sha1(bytes(AdminEntry.get(), 'utf-8')).hexdigest(), open("AdminCode.p", "wb") )
    print("ADMIN PASSWORD CREATED")
    programlist()
def SigninAdmin():
    if hashlib.sha1(bytes(AdminEntry.get(), 'utf-8')).hexdigest() == pickle.load( open( "AdminCode.p", "rb" ) ):
        labelUser.pack_forget()
        AdminEntry.pack_forget()
        AdminSubmit.pack_forget()
        AdminS = True
        programlist()
    else:
        exit()
def games():
    programbox.config(textvariable = program, value = ())
    startprogram.config(text = "Start Program", command = gamestart)
    labelUser.config(foreground = "black", text = "Games")
    programbox.config(textvariable = program, value = ("Flappy Bird","Sign Out"))
    programbox.pack()
    startprogram.config(text = "Start Program", command = programstart)
    startprogram.pack()
def fileexplorer():
    forgetA()
    docnames = pickle.load( open( "docNames.p", "rb" ) )
    if docnames[0] == "":
        while docnames[0] == "":
            docnames.pop(0)
    printassist = 0
    filesystem.pack()
    for i in range(0,len(docnames)-2):
        filesystem.insert("", "end", docnames[i], text = docnames[i])
    filesystem.config(selectmode = "browse")
    fileOpen.config(text = "Open", command = openFile)
    fileExit.config(text = "Exit", command = exitfile)
    fileDelete.config(text = "Delete", command = deleteFile)
    fileOpen.pack()
    fileExit.pack()
    fileDelete.pack()
def openFile():
    filesystem.pack_forget()
    fileOpen.pack_forget()
    fileExit.pack_forget()
    fileDelete.pack_forget()
    Text.config(width = 50, height = 20, wrap = "word")
    TeditSave.config(text = "Save", command = fileSave)
    TeditExit.config(text = "Exit", command = exittext)
    Text.pack()
    TeditSave.pack()
    TeditExit.pack()
    Text.insert("1.0", pickle.load( open("".join(filesystem.selection()) + ".p", "rb" )))
def fileSave():
    pickle.dump( Text.get('1.0', 'end'), open( "".join(filesystem.selection())+".p", "wb" ) )
def exitfile():
    filesystem.pack_forget()
    fileOpen.pack_forget()
    fileExit.pack_forget()
    fileDelete.pack_forget()
    filesystem.delete(*filesystem.get_children())
    Text.delete("1.0","end")
    programlist()
def deleteFile():
    delFileN = pickle.load( open( "docNames.p", "rb" ) )
    delFileN.pop(delFileN.index("".join(filesystem.selection())))
    os.remove("".join(filesystem.selection())+".p")
    filesystem.delete(filesystem.selection())
    pickle.dump(delFileN, open( "docNames.p", "wb" ) )
def textedit():
    forgetA()
    filelabel.config(text = "File Name")
    filename.config(width = 30)
    Text.config(width = 50, height = 20, wrap = "word")
    TeditSave.config(text = "Save", command = savetext)
    TeditExit.config(text = "Exit", command = exittext)
    filelabel.pack()
    filename.pack()
    Text.pack()
    TeditSave.pack()
    TeditExit.pack()

def exittext():
    filelabel.pack_forget()
    filename.pack_forget()
    Text.pack_forget()
    TeditSave.pack_forget()
    TeditExit.pack_forget()
    filesystem.delete(*filesystem.get_children())
    filename.delete(0, END)
    Text.delete("1.0","end")
    programlist()
    
def savetext():
    pickle.dump( Text.get('1.0', 'end'), open( filename.get()+".p", "wb" ) )
    nameSave = pickle.load( open( "docNames.p", "rb" ) )
    nameSave.insert(0, filename.get())
    pickle.dump( nameSave, open( "docNames.p", "wb" ) )
    
def calc():
    forgetA()
    goforward.pack_forget()
    answer.pack_forget()
    symSense = StringVar()
    num1 = IntVar()
    num2 = IntVar()
    labelUser.config(text = "Calculator")
    labelUser.pack()
    box1.config(width = 30)
    sym.config(textvariable = symSense,value = ("*","/","+","-","exponent","sqrt","Go To Main Menu"))
    box2.config(width = 30)
    box1.pack()
    sym.pack()
    box2.pack()
    evaluate.config(text = "Calculate", command = CalculateFinal)
    evaluate.pack()

def CalculateFinal():
    box1.pack_forget()
    sym.pack_forget()
    box2.pack_forget()
    evaluate.pack_forget()
    if sym.get() == "sqrt" or "exponent" or "Go To Main Menu" or "":
        if sym.get() == "sqrt":
            answer.config(text = math.sqrt(float(box1.get())))
            answer.pack()
            time.sleep(3)
            answer.pack_forget()
            calc()
        if sym.get() == "exponent":
            answer.config(text = int(box1.get())**int(box2.get()))
            answer.pack()
            time.sleep(3)
            answer.pack_forget()
            calc()
        if sym.get() == "Go To Main Menu":
            programlist()
            goforward.pack_forget()
        if sym.get() == "":
            sym.set("*")
    calcAssist = box1.get() + sym.get() + box2.get()
    answer.config(text = eval(calcAssist))
    answer.pack()
    goforward.config(text = "Continue", command = calc)
    goforward.pack()
def signin():
    forgetA()
    if hashlib.sha1(bytes(username.get(), 'utf-8')).hexdigest() == pickle.load( open( "Username.p", "rb" ) ) and hashlib.sha1(bytes(password.get(), 'utf-8')).hexdigest() == pickle.load( open( "Password.p", "rb" ) ):
        print ("SIGN IN SUCCESFUL")
        return True
    else:
        labelUser.config(foreground = "red", text = "Username: NOT ACCEPTED")
        labelPass.config(foreground = "red", text = "Password: NOT ACCEPTED")
        print ("error")
def signinbox():
    signup = Checkbutton(root, text = "Sign Up", variable = v)
    labelUser = ttk.Label(root, text = "Username:")
    username = ttk.Entry(root, width = 30)
    labelPass = ttk.Label(root, text = "Password:")
    password = ttk.Entry(root, width = 30, show = "*")
    labelUser.pack()
    username.pack()
    labelPass.pack()
    password.pack()
    clear = ttk.Button(root, text = "Clear", command = clearentry)
    submit = ttk.Button(root, text = "Submit", command = submitentry)
    clear.pack()
    submit.pack()
    signup.pack()
    mainloop()

# Starting Code
root.title("Simple OS GUI")
signup = Checkbutton(root, text = "Sign Up", variable = v)
labelUser = ttk.Label(root, text = "Username:")
username = ttk.Entry(root, width = 30)
labelPass = ttk.Label(root, text = "Password:")
password = ttk.Entry(root, width = 30, show = "*")
labelUser.pack()
username.pack()
labelPass.pack()
password.pack()
clear = ttk.Button(root, text = "Clear", command = clearentry)
submit = ttk.Button(root, text = "Submit", command = submitentry)
clear.pack()
submit.pack()
signup.pack()
mainloop()
