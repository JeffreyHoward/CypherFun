import Cyphers
import FrequencyCounter as freq
import CaesarFrequencyAnalysis as analysis
import sys

def main():

    cyphertext = open(sys.argv[1], "r+").read()
    outfile = sys.argv[2]

    cypherFreq = freq.freqTable(cyphertext)

    shift = analysis.findkey(cypherFreq, "gutenburg.csv")

    outfile = open(outfile, "w+")

    outfile.write(Cyphers.Caesar("-d", shift, cyphertext))

    outfile.close()

if __name__ == "__main__":
    main()