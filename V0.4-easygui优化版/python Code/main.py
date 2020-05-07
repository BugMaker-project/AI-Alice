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
        break
    else:
        reponse=alice.respond(Command)
        easygui.msgbox(reponse)
