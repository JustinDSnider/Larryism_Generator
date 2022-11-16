def ReadFile(fileName):
    f = open(f"Resources/PhraseParts/{fileName}.txt", "r")
    rawPhrasePart = f.readlines()
    f.close()
    PhrasePart = []
    for i in range(len(rawPhrasePart)):
        PhrasePart.append(rawPhrasePart[i].strip('\n'))
    return PhrasePart