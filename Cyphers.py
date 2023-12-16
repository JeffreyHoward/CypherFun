import sys

def main():

    plainfile = open(sys.argv[1], 'r+')
    cypherfile = open(sys.argv[2], 'w+')
    key = sys.argv[3]

    mode = '-e'
    cypher = '-c'

    for i in sys.argv:
        if i == '-e':
            mode = i
        if i == '-d':
            mode = i
        if i == '-c':
            cypher = i
        if i == '-p':
            cypher = i
        if i == '-v':
            cypher = i

    match cypher:
        case "-c":
            cyphertext = Caesar(mode, key, plainfile.read())
        case "-p":
            cyphertext = Permutation(mode, key, plainfile.read())
        case "-v":
            cyphertext = Vingere(mode, key, plainfile.read())

    cypherfile.write(cyphertext)
    plainfile.close()
    cypherfile.close()

    exit()

def CaesarShift(char, shift):
    new = ord(char) + shift
    if new > ord('~'):
        new = ((new - ord(' ')) % (127 - ord(' '))) + ord(' ')
    if new < ord(' '):
        new = ((new - 127) % (127 - ord(' '))) + ord(' ')
    return chr(new)

def Caesar(mode, shift, message):
    shift = int(shift)
    if mode == '-d':
        shift *= -1
    return ''.join(CaesarShift(i, shift) for i in message)

def Permutation(mode, pfile, message):
    map = {}
    pfile = open(pfile, "r")

    if mode == "-e":
        index = 0
        outdex = 1
    if mode == "-d":
        index = 1
        outdex = 0
    
    for i in pfile.readlines():
        map[i[index]] = i[outdex]
    new = []
    for i in message:
        if i in map:
            new.append(map[i])
        else:
            new.append(i)
    pfile.close()
    return ''.join(new)

def Vingere(mode, keyword, message):
    if mode == '-e':
        fac = 1
    else:
        fac = -1
    return ''.join(CaesarShift(message[i], fac * ord(keyword[i % len(keyword)])) for i in range(len(message)))
    
if __name__ == "__main__":
    main()