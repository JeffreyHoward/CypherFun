# CypherFun

This is a small project to get some more hands on experience working with encryption by implementing some basic cyphers (Caesar, Permutation, Vingere) and attacks against them (Only Caesar so far). All testing and reference data comes from Project Gutenburg.

The Cyphers.py file performs the encryption and decryption given plaintext and a key. It takes flags to specify the mode and type of cypher: 

Cyphers.py [input plaintext] [output cyphertext] [key]

-e   Encrypts input text (default)
-d   Decrypt input text
-c   Caesar cypher takes an integer as a key (default) 
-p   Perutation cypher takes a file describing the mappings similar to permute.txt
-v   Vingere cypher takes an ASCII word as a key

The FrequencyCounter.py file is for counting the frequency of characters in a file and creating a .csv file from that data:

FrequencyCounter.py [input plaintext] [output csv]

-N   Normalizes the CSV table so it reflects a character probability rather than a frequency
-D   Takes a folder full of files as input and counts the frequency of characters over the files in the forlder
-G   Performs the frequency count over the first 40 books of Project Gurenberg, used as a stand in for the character frequencies of the English language
-U   Takes a the URL of a .txt as input text

The CaesarFrequencyAnalysis takes the normalized frequency tables for some cyphertext and some reference frequency table and guesses the Caesar shift that was applied to the cypher text. It does this by considering all possible shifts and taking that which is most similar to the reference:

CaesarFrequencyAnalysis.py [cyphertext frequency table] [reference frequency table]

CaesarDecrypt this is the culminating file of this project as of now, it takes in only some cyphertext and uses the rest of the files to output the predicted decrypted plaintext.

CaesarDecrypt.py [input cyphertext] [output decrypted text]