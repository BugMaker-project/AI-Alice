import bots
import os
import time
os.chdir('./Data') 
alice = bots.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')
print("Exit command is 'EXIT'")
while True:
    Command=input(">>>")
    if Command=="EXIT" or \
       Command=="Exit" or\
       Command=="exit" or \
       Command=="EXit" or \
       Command=="EXIt":
        print("Bye!")
        time.sleep(2)
        break
    else:
        reponse=alice.respond(Command)
        time.sleep(0.5)
        print(reponse)
        time.sleep(0.3)
