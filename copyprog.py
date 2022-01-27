import shutil

path = [
    input("source path="),
    input("destination=")
]

def copy():
    shutil.copy(path[0],path[1])



def copydata():
    shutil.copyfile(path[0],path[1])
