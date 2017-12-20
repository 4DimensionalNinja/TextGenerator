import random,re
from bb_FileWords import FileWords

inputPath = 'input'
outputPath = 'bbrett_output.txt'

def fileAllowed(file):
    """Determines which scanned files will be processed"""
    if file.is_file() and file.name.lower().endswith('.txt'):
        return True
    else:
        return False


l = 50
listOut = []

outputFile = open(outputPath, 'w')

with os.scandir(inputPath) as l:
    for n in l:
        if n.is_file() and fileAllowed(n):
            fileList.append(FileWords(n.path))

while(len(listOut) < 3):
    listOut.append(random.choice(corpus))

for i in range(2, l - 1):
    possible = []
    possible3 = []
    possible2 = []
    possible1 = []
    outputFile.write('Word ' + str(i) + '\n')
    
    for j in range(len(corpus)- 3):
        if listOut[i-2] == corpus[j] and listOut[i-1] == corpus[j+1] and listOut[i] == corpus[j+2]:
            outputFile.write(str(corpus[j:j+4]) + '\n')
            possible3.append(corpus[j+3])

    if len(possible3) < 2:
        for j in range(len(corpus)-2):
            if listOut[i-1] == corpus[j] and listOut[i] == corpus[j+1]:
                outputFile.write(str(corpus[j:j+3]) + '\n')
                possible2.append(corpus[j+2])

    if len(possible3) < 2 and len(possible2) < 2:
        possible = possible * 2
        for j in range(len(corpus)-1):
            if listOut[i] == corpus[j]:
                outputFile.write(str(corpus[j:j+2]) + '\n')
                possible1.append(corpus[j+1])

    possible = 3*possible3 + 2*possible2 + possible1
    outputFile.write('Possible: ' + str(possible) + '\n\n')

    if len(possible) > 0:
        listOut.append(random.choice(possible))
    else:
        listOut.append(random.choice(corpus))

print(listOut)
outputFile.close()
