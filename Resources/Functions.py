from datetime import datetime as dt

def getDay():
    return dt.now().strftime('%A')

def readFile(fileName):
    f = open(f"Resources/{fileName}.txt", "r")
    List = f.readlines()
    f.close()
    List2 = []
    for i in range(len(List)):
        List2.append(List[i].strip('\n'))
    return List2