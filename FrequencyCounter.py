import sys
import csv
import string
import os

def main():

    normed = False
    folder = False
    for arg in sys.argv:
        if arg == "-N":
            normed = True
        if arg == "-F":
            folder == True
    if folder:
        text = ''
        for filename in os.listdir(sys.argv[1]):
            filename = os.path.join(sys.argv[1], filename)
            
    else:
        text = open(sys.argv[1], "r+")

    with open(sys.argv[2], 'w+') as file:
        writer = csv.writer(file)
        writer.writerow(["Character", "Frequency"])
        table = freqTable(text.read())
        if normed:
            table = list(map(lambda x: x / sum(table), table))
        for i in range(len(table)):
            writer.writerow([chr(i + ord(" ")), table[i]])
        file.close()
    text.close()
     

def freqTable(text):
    table = [0] * (ord("~") - ord(" ") + 1)
    for i in text:
        table[ord(i) - ord(" ")] += 1
    return table

if __name__ == "__main__":
    main()