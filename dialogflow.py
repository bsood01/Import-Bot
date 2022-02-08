import shutil
import os

shutil.unpack_archive("PizzaBot.zip","./direct")
fhandle = open("./direct/agent.json", 'r')
for i in fhandle:
    print(i)
files = os.listdir("./direct/intents")
for i in files:
    fhandle = open('./direct/intents/'+i, 'r')
    for j in fhandle:
        print(j)
files = os.listdir("./direct/entities")
for i in files:
    fhandle = open('./direct/entities/'+i,'r')
    for j in fhandle:
        print(j)

shutil.rmtree("./direct")
