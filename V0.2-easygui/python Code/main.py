import bots
import os
import time
import easygui
os.chdir('./Data') 
alice = bots.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')
easygui.msgbox("Exit command is 'EXIT'")
while True:
    Command=easygui.enterbox("QuestionHere>>")
    if Command=="EXIT":
        easygui.msgbox("Bye!")
        time.sleep(2)
        break
    else:
        reponse=alice.respond(Command)
        time.sleep(0.5)
        easygui.msgbox(reponse)
        time.sleep(0.3)
