import random
import math
import time
import pickle
import base64

loop = 0
signin = ""
signedin = 0
def space(a):
    loop = 0
    while loop < a:
        print (" ")
        loop += 1
def signin():
    space(3)
    usernamesignin = str(input("Username: "))
    passwordsignin = str(input("Password: "))
    if base64.b64encode(bytes(usernamesignin, 'utf-8')) == pickle.load( open( "Username.p", "rb" ) ) and base64.b64encode(bytes(passwordsignin, 'utf-8')) == pickle.load( open( "Password.p", "rb" ) ):
        print ("SIGN IN SUCCESFUL")
        space(2)
        print("Hi ", usernamesignin)
        return True
    else:
        Print ("error")
def programlist():
    space(2)
    print("1. dice game")
    print("2. calculator")
    print("3. cipher(folder)")
    print("4. text editor")
    print("5. file explorer")
    print("6. random generator")
    print("7. sign out")
    space(1)
    programnum = str(input("input the program: "))
    if programnum == "1":
        dice()
    elif programnum == "2":
        calc()
    elif programnum == "4":
        space(1)
        print("to stop program type *STOP* in all caps \n on its own line.")
        space(1)
        docbetween = str(input("Document Name? "))
        textedit(docbetween)
    if programnum == "7":
        if signin() == True:
            programlist()
    elif programnum == "3":
        space(2)
        print("1a. shift cipher")
        print("2a.polyalphabetic cipher")
        programnum = str(input("input the program: "))
    elif programnum == "5":
        space(1)
        fileExplorer()
    elif programnum == "6":
        randomgen()
    if programnum == "1a":
        cipher1()
    elif programnum == "2a":
        cipher2()
def randomgen():
    z = 1
    a = 0
    b = 0
    c = 0

    print("Diamond Studios 2016")
    time.sleep(2)
    print("Random Generator V3 Loading...")
    time.sleep(2)
    while z==z:
        print("    ")
        print("    ")
        print("A >> Random Number 1-100")
        print("B >> Random Number 1-500")
        print("C >> Random Number 1-1000")
        print("D >> Custom Random ?-?")
        print("E >> Custom List Selector")
        print("F >> Dice Roll")
        print("G >> Whats New In 3.0?")
        print("H >> Credits")
        print("I >> More")
        print("J >> Stop")
        sym = str(input("Please Select a Function: "))
        if sym == "A":
            print("    ")
            print("    ")
            print("Chosing Number 1-100...")
            time.sleep(2)
            a = random.randint(1,100)
            print(a)
            time.sleep(2)
        if sym == "B":
            print("    ")
            print("    ")
            print("Chosing Number 1-500...")
            time.sleep(2)
            b = random.randint(1,500)
            print(b)
            time.sleep(2)
        if sym == "C":
            print("    ")
            print("    ")
            print("Chosing Number 1-1000...")
            time.sleep(2)
            c = random.randint(1,1000)
            print(c)
            time.sleep(2)
        if sym == "D":
            print("    ")
            print("    ")
            int1 = int(input("Please Chose First Integer: "))
            int2 = int(input("Please Chose Second Integer: "))
            if int2 > int1:
                print("Chosing Random Number...")
                final = random.randint(int1, int2)
                print(final)
                time.sleep(2)
            else:
                print("Chosing Random Number...")
                final = random.randint(int2, int1)
                print(final)
                time.sleep(2)
        if sym == "E":
            print("    ")
            print("    ")
            ask = (str(input("Is this going to be Numbers(N) or Words(W): ")))
            if ask == "N":
                print("    ")
                print("    ")
                List = [int(input("Item 1: ")),int(input("Item 2: ")),int(input("Item 3: ")),int(input("Item 4: ")),int(input("Item 5: "))]
                print(List[random.randint(1,len(List))])
                time.sleep(2)
            if ask == "W":                
                print("    ")
                print("    ")
                List = [str(input("Item 1: ")),str(input("Item 2: ")),str(input("Item 3: ")),str(input("Item 4: ")),str(input("Item 5: "))]
                print("    ")
                print("    ")
                print(List[random.randint(1,len(List))])
                time.sleep(2)
        if sym == "F":
            print("    ")
            print("    ")
            print("   _______ ")           
            print("  /\       \ ")           
            print(" /()\   ()  \ ")         
            print("/    \_______\ ")         
            print("\    /()     /")         
            print(" \()/   ()  /")          
            print("  \/_____()/")
            time.sleep(1)
            print("Rolling...")
            print("    ")
            print("    ")
            time.sleep(2)
            dice = random.randint(1,6)
            print("You got...")
            print("    ")
            print("    ")
            time.sleep(1)
            print(dice)
            time.sleep(2)
        if sym == "G":
            print("    ")
            print("    ")
            print("Newer Design - Fixes - Simpler - More Customization - Added Spacing - New Options")
            time.sleep(2)
        if sym == "H":
            print("    ")
            print("    ")
            print("Random Generator V3")
            time.sleep(2)
            print("Diamond Studios 2016")
            time.sleep(2)
            print("& Carson Ott")
            time.sleep(2)
            print("Main Coding: Ashton Smith")
            time.sleep(2)
            print("Foundation: Ashton Smith")
            time.sleep(2)
            print("Advanced Syntax: Carson Ott")
            time.sleep(2)
        if sym == "I":
            print("    ")
            print("    ")
            print("Try Some Other Diamond Studio Programs!")
            time.sleep(2)
            print("SimpleMath, MasterOS, & More to Come!")
            time.sleep(2)
            print("Also check out Carson Ott's creations!")
            time.sleep(2)
        if sym == "J":
            space(1)
            print("stopping...")
            delay(.5)
            programlist()
def fileExplorer():
    fileNames = pickle.load( open( "docNames.p", "rb" ) )
    loop = 0
    num = 1
    while loop <= len(fileNames)-1:
        print(num,"."," ",fileNames[num - 1])
        num += 1
        loop += 1
    docnum = int(input("which would you like to open? "))
    space(1)
    docnum -= 1
    opendoc = pickle.load( open( fileNames[docnum]+".p", "rb" ) )
    printdoc = 0
    loop = 0
    while loop <= len(opendoc) - 1:
        print(opendoc[printdoc])
        printdoc += 1
        loop += 1
    doc = []
    while 1 == 1:
        line = 0
        lineprint = 0
        textLine = str(input(""))
        if textLine == "*STOP*":
            pickle.dump( doc, open( fileNames[docnum]+".p", "wb" ) )
            space(1)
            print("Doc saved!")
            programlist()
        doc.insert(line, textLine)
        line += 1
def textedit(docName):
    doc = []
    while 1 == 1:
        line = 0
        lineprint = 0
        textLine = str(input(""))
        if textLine == "*STOP*":
            pickle.dump( doc, open( docName+".p", "wb" ) )
            try:
                nameSave = pickle.load( open( "docNames.p", "rb" ) )
            except:
                pickle.dump([],open("docNames.p", "wb"))
                nameSave = pickle.load( open("docNames.p", "rb"))
            nameSave.insert(0,docName)
            pickle.dump( nameSave, open( "docNames.p", "wb" ) )
            space(1)
            print("Doc saved!")
            programlist()
        doc.insert(line, textLine)
        line += 1
"""
                while loop <= len(doc):
                    print(doc[lineprint])
                    lineprint += 1
                lineprint = 0
"""
def cipher2():
    message = str(input("message plz. no caps, no punctuation, no numbers. "))
    # message input.
    strShiftKey = str(input("letter shift word plz. no numbers. "))
    # ceasar cipher shift amount.
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    lShiftWord = []
    # Number equivelents for strShiftKey
    iShiftWordNum = 0
    iAlphNum = 0
    # helps find letter from alphabet
    iAlphShiftNum = 0
    # alphabet assist for encryption adds shift in
    iMessageData = 0
    # how far into message encryption the program is
    strResult = " "
    strResult1 = " "
    # message result (encoded)
    while iMessageData < len(strShiftKey):
        if alphabet[iAlphNum] in strShiftKey[iMessageData]:
            print (" ")
            while iAlphNum > 26:
                iAlphNum = iAlphNum - 27
                # checks if the alph num is over string length
            lShiftWord.append (iAlphNum)
            # adds number to shift word list
            iMessageData = iMessageData + 1
            iAlphNum = 0
        else:
            iAlphNum = iAlphNum + 1
            # if the letter tried does not come out true a differnt letter is tried
    iMessageData = 0
    while iMessageData < len(message):
        if alphabet[iAlphNum] in message[iMessageData]:
            print (" ")
            iAlphShiftNum = iAlphNum + lShiftWord[iShiftWordNum]
            while iAlphShiftNum > 26:
                iAlphShiftNum = iAlphShiftNum - 27
            strResult1 = alphabet[iAlphShiftNum]
            strResult = strResult + strResult1
            # renders answer
            iMessageData = iMessageData + 1
            # changes what letter program is evaluated 
            iAlphNum = 0
            if iShiftWordNum == (len(lShiftWord) - 1):
                iShiftWordNum = 0
                # siplifies expresion if over allowed amount
            else:
                iShiftWordNum = iShiftWordNum + 1
            # if the letter tried does not come out true a differnt letter is tried
    #       if messrec == len(shiftword)-1:
    #            messloop = 0
        else:
            iAlphNum = iAlphNum + 1
    print (strResult)
    cont()
    cipher2()
def cipher1():
    message = str(input("message plz. no caps, no punctuation, no numbers. "))
    # message (input).
    shift = float(input("letter shift plz no decimials. "))
    # ceasar cipher shift amount.
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    ciALPH = 0
    # alphabet assist for encryption
    ciMESS = 0
    # how far into message encryption the program is
    mR = " "
    # message result (encoded)
    while ciMESS < len(message):
        if alphabet[ciALPH] in message[ciMESS]:
            print ("True")
            cialphsh = 2
            cialphsh = int(ciALPH + shift)
            while cialphsh >= 26:
                cialphsh = cialphsh - 26
                print ("simplified")
                print (cialphsh)
                if cialphsh == 0 or cialphsh == 1 or cialphsh <= 10:
                    break
            while cialphsh <= 0:
                cialphsh = cialphsh + 26
            mR1 = alphabet[cialphsh]
            mR = mR + mR1
            ciMESS = ciMESS + 1
            ciALPH = 0
        else:
            ciALPH = ciALPH + 1
    print (mR)
    cont()
    cipher1()
def dice():
    print("1. Game")
    print("2. Roll Generator")
    space(1)
    loop = 0
    score = 0
    count = 0
    version = int(input("Game or roll generator? "))
    if version == 1:
        print("version accepted")
        print("In this simple game you guess the outcome of the die to score points!")
        dieNum = float(input("how many dice(1-6)? "))
        d1 = 6
        d2 = 6
        d3 = 6
        d4 = 6
        d5 = 6
        d6 = 6
    if version == 2:
        if str(input("Ready(Y/N)? ")) == "Y":
            dieNum = float(input("how many dice(1-6)? "))
            if dieNum == 1:
                d1 = float(input("How many sides on die 1? "))
            if dieNum == 2:
                d1 = float(input("How many sides on die 1? "))
                d2 = float(input("How many sides on die 2? "))
            if dieNum == 3:
                d1 = float(input("How many sides on die 1? "))
                d2 = float(input("How many sides on die 2? "))
                d3 = float(input("How many sides on die 3? "))
            if dieNum == 4:
                d1 = float(input("How many sides on die 1? "))
                d2 = float(input("How many sides on die 2? "))
                d3 = float(input("How many sides on die 3? "))
                d4 = float(input("How many sides on die 4? "))
            if dieNum == 5:
                d1 = float(input("How many sides on die 1? "))
                d2 = float(input("How many sides on die 2? "))
                d3 = float(input("How many sides on die 3? "))
                d4 = float(input("How many sides on die 4? "))
                d5 = float(input("How many sides on die 5? "))
            if dieNum == 6:
                d1 = float(input("How many sides on die 1? "))
                d2 = float(input("How many sides on die 2? "))
                d3 = float(input("How many sides on die 3? "))
                d4 = float(input("How many sides on die 4? "))
                d5 = float(input("How many sides on die 5? "))
                d6 = float(input("How many sides on die 6? "))
    while loop == 0:

#        sense = str(input("Ready(Y/N/STOP)? "))
#        if sense == "STOP":
#            print ("stopping...")
#            print ("STOPPED")
#            programlist()
#        if sense == "Y":
        from random import randint
        if version == 1:
            DiceGuess = int(input("What is your guess?" ))
        if dieNum == 1:
            ans1 = randint(1, d1)
            print (ans1)
            count = count + 1
        if dieNum == 2:
            ans1 = randint(1, d1)
            ans2 = randint(1, d2)
            print (ans1, ans2)
            print ("Total =",ans1+ans2)
            count = count + 1
        if dieNum == 3:
            ans1 = randint(1, d1)
            ans2 = randint(1, d2)
            ans3 = randint(1, d3)
            print (ans1, ans2, ans3)
            print ("Total =",ans1+ans2+ans3)
            count = count + 1
        if dieNum == 4:
            ans1 = randint(1, d1)
            ans2 = randint(1, d2)
            ans3 = randint(1, d3)
            ans4 = randint(1, d4)
            print (ans1, ans2, ans3, ans4)
            print ("Total =",ans1+ans2+ans3+ans4)
            count = count + 1
        if dieNum == 5:
            ans1 = randint(1, d1)
            ans2 = randint(1, d2)
            ans3 = randint(1, d3)
            ans4 = randint(1, d4)
            ans5 = randint(1, d5)
            print (ans1, ans2, ans3, ans4, ans5)
            print ("Total =",ans1+ans2+ans3+ans4+ans5)
            count = count + 1
        if dieNum == 6:
            ans1 = randint(1, d1)
            ans2 = randint(1, d2)
            ans3 = randint(1, d3)
            ans4 = randint(1, d4)
            ans5 = randint(1, d5)
            ans6 = randint(1, d6)
            print (ans1, ans2, ans3, ans4, ans5, ans6)
            print ("Total =",ans1+ans2+ans3+ans4+ans5+ans6)
            count = count + 1
        if version == 1:
            if DiceGuess == ans1:
                print("good job!!!")
                print ("score plus", 80 + 15 * dieNum ,"!!!")
                score += 80 + 15 * dieNum
                print("Your Score Is - ",score)
            elif DiceGuess == ans1 - 1 or DiceGuess == ans1 + 1:
                print("good job!!!")
                print ("score plus", 10 + 2 * dieNum, "!!!")
                score += 10 + 3 * dieNum
                print("Your Score Is - ",score)
            else:
                print("sorry you guessed incorrectly!")
                print("Your Score Is - ",score)
        if count == 5 and version == 1:
            cont()
        if count == 10 and version == 2:
            cont()
            if str(input("Run settup again(Y/N)? ")) == "Y":
                dieNum = float(input("how many dice(1-6)? "))
                if dieNum == 1:
                    d1 = float(input("How many sides on die 1? "))
                if dieNum == 2:
                    d1 = float(input("How many sides on die 1? "))
                    d2 = float(input("How many sides on die 2? "))
                if dieNum == 3:
                    d1 = float(input("How many sides on die 1? "))
                    d2 = float(input("How many sides on die 2? "))
                    d3 = float(input("How many sides on die 3? "))
                if dieNum == 4:
                    d1 = float(input("How many sides on die 1? "))
                    d2 = float(input("How many sides on die 2? "))
                    d3 = float(input("How many sides on die 3? "))
                    d4 = float(input("How many sides on die 4? "))
                if dieNum == 5:
                    d1 = float(input("How many sides on die 1? "))
                    d2 = float(input("How many sides on die 2? "))
                    d3 = float(input("How many sides on die 3? "))
                    d4 = float(input("How many sides on die 4? "))
                    d5 = float(input("How many sides on die 5? "))
                if dieNum == 6:
                    d1 = float(input("How many sides on die 1? "))
                    d2 = float(input("How many sides on die 2? "))
                    d3 = float(input("How many sides on die 3? "))
                    d4 = float(input("How many sides on die 4? "))
                    d5 = float(input("How many sides on die 5? "))
                    d6 = float(input("How many sides on die 6? "))
            count = 0
def delay(a):
    time.sleep(a)
def calc():
    import math
    x = 0
    loop = 0
    while loop == 0:
        x = x + 1
        print ("....")
        print ("......")
        print ("........")
        print ("......")
        print ("....")
        if x == 5:
            loop = 10
    while loop == 10:
        print("   ")
        print("SYMBOLS:")
        print ("1. *")
        print ("2. /")
        print ("3. -")
        print ("4. +")
        print ("5. sqrt")
        print ("6. exponent")
        print ("7. stop")
        print("   ")
        sym = str(input("symbol plz. "))
        if sym == "7" or sym == "stop":
            stopYN = str(input("are u sure (Y/N)? "))
            if stopYN == "Y":
                break
        int1 = float(input("Number 1 plz. "))
        if not sym == "5":
            if not sym == "sqrt":
                int2 = float(input("Number 2 plz. "))
        print ("   ")
        if sym == "1" or sym == "*":
            print (int1 * int2)
        if sym == "2" or sym == "/":
            print (int1 / int2)
        if sym == "3" or sym == "-":
            print (int1 - int2)
        if sym == "4" or sym == "+":
            print (int1 + int2)
        if sym == "5" or sym == "sqrt":
            sqrt = math.sqrt(int1)
            print (sqrt)
        if sym == "6" or sym == "exponent":
            print (int1 ** int2)
        print ("   ")
        cont()
def cont():
    cont = str(input("continue this programY/N? "))
    if cont == "N":
        programlist()
        return "stop"
while loop < 3:
    print(".")
    print("..")
    print("...")
    print("....")
    print(".....")
    print("....")
    print("...")
    print("..")
    print(".")
    loop += 1
print ("INSTALLATION - SUCSESSFUL")
print ("Simple OS Ready for use")
loop = 0
space(5)
try:
    open("Password.p","rb")
except:
    if str(input("make a new userY/N? ")) == "Y":
        pickle.dump( base64.b64encode(bytes(str(input("Create a Username: ")), 'utf-8')), open( "Username.p", "wb" ) )
        print ("USER CREATED")
        pickle.dump( base64.b64encode(bytes(str(input("Create a Password: ")), 'utf-8')), open( "Password.p", "wb" ) )
        print ("PASSWORD CREATED")
if signin() == True:
    space(1)
    programlist()
