import random,re

inputPath = 'input.txt'
outputPath = 'bbrett_output.txt'
l = 50
listOut = []
k = 0

def simplifyWord(wordIn):
    wordOut = wordIn.lower()
    wordOut = wordOut.rstrip(',;.:)]\"')
    wordOut = wordOut.lstrip(',;.:([\"')

    return wordOut

def simplifyWordPart(wordIn):
    wordOut = wordIn.lower()
    wordOut = wordOut.rstrip(')]\"')
    wordOut = wordOut.lstrip('([\"')
    
    return wordOut

def countEndPunct(wordIn):
    if wordIn.endswith((',' , ';' , '.' , ':')):
        return 1
    return 0

inputFile = open(inputPath, 'r')
outputFile = open(outputPath, 'w')

fullText = inputFile.read()
inputFile.close()

corpus = fullText.split()

while k < len(corpus):
    current = k
    n = countEndPunct(corpus[current])
    if n > 0:
        corpus.insert(k+1, corpus[current][-n])
        k += 1
    corpus[current] = simplifyWord(corpus[i])
    k += 1

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
