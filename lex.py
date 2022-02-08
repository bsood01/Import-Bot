import shutil
import os

def isFile(name):
    name_split = name.split(".")
    return len(name_split) == 2


shutil.unpack_archive("BookTrip-DRAFT-JE5ZNHCPB5-LexJson.zip","./direct")
direct_queue = ["./direct"]
file_lst = []
while len(direct_queue) > 0:
    current_direct = direct_queue.pop(0)
    content = os.listdir(current_direct)
    for i in content:
        if isFile(i):
            file_lst.append(current_direct+"/"+i)
        else:
            direct_queue.append(current_direct+"/"+i)
for i in file_lst:
    with open(i, 'r') as f:
        print(f.read())

shutil.rmtree("./direct")
