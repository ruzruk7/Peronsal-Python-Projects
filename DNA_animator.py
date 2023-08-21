import random, sys, time
delay = 0.10

ROWS = [
    #123456789 <- Use this to measure the number of spaces:
    '         ##',  # Index 0 has no {}
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '     #{}-----{}#',
    '     #{}----{}#',
    '      #{}---{}#',
    '       #{}-{}#',
    '        ##',
    '       #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '      #{}------{}#',
    '       #{}-----{}#',
    '        #{}---{}#',
    '         #{}-{}#']
    #123456789
try:
    print("DNA Animation")
    time.sleep(2)
    rowIndex = 0

    while True: # main program loop
        # increment rowIndex to draw next row:
        rowIndex += 1
        if rowIndex == len(ROWS):
            rowIndex = 0
        
        # Row Indexes 0 and 9 dont have nucleotides
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue
    
        # select random nucleotide pais, guanine-cytosine and adenine-thymine:
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = ('A'), ('T')
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = ('T'), ('A')
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = ('C'), ('G')
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = ('G'), ('C')

        # Print the row.
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(delay)
except KeyboardInterrupt:
    sys.exit()



