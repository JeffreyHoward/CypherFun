import csv
import sys

def main():
    
    print(findkey(sys.argv[1], sys.argv[2]))

def findkey(cypherdata, corpusdata):
    if ".csv" in cypherdata:
        cypherdata = list(csv.reader(open(cypherdata, "r"), dialect = 'excel'))[1:]
        cypherdata = list((float(i[1]) for i in cypherdata))

    if ".csv" in corpusdata:
        corpusdata = list(csv.reader(open(corpusdata, "r"), dialect = 'excel'))[1:]
        corpusdata = list((float(i[1]) for i in corpusdata))

    min_shift = 0
    min = chi_squared(cypherdata, corpusdata)
    alphabet_len = len(cypherdata)
    for i in range(1, alphabet_len - 1):
        score = chi_squared(cypherdata[(alphabet_len - i - 1):] + cypherdata[:(alphabet_len - i - 1)], corpusdata)
        if score < min:
            min = score
            min_shift = i
    
    return (min_shift * -1) % 94

def chi_squared(observed, expected):
    sum = 0
    for char in zip(observed, expected):
        sum += ((char[0] - char[1]) ** 2)/char[1]
    return sum

if __name__ == "__main__":
    main()