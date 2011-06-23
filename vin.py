import random

vinDigitPositionMultiplier = [ 8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2 ]
vinDigitValues = { 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'J':1,
                        'K':2, 'L':3, 'M':4, 'N':5, 'P':7, 'R':9, 'S':2, 'T':3, 'U':4, 'V':5, 
                        'W':6, 'X':7, 'Y':8, 'Z':9, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, 
                        '7':7, '8':8, '9':9, '0':0}

class VinYear:
    def __init__(self, first8, year):
        self.First8 = first8
        self.Year = year
    
    def __repr__(self):
        return "First8: %s - Year: %s" % (self.First8, self.Year)

def getRandomVin():
    vinYear = getRandomVinStart()
    char = getRandomVinChar()
        
    v = "%s%s%s" % (vinYear.First8, char, vinYear.Year)
    for i in range(7):
        v += getRandomVinChar()
            
    checkChar = getCheckSumChar(v)
    v = "%s%s%s" % (v[0:8], checkChar, v[9:])
    return v

def getCheckSumChar(vin):
    # generate the check sum
    checkSumTotal = 0

    if (len(vin) < 17):
        print "Invalid Length: %s" % len(vin)
        return -1

    for i in range(len(vin)):
        if (vinDigitValues.get(vin[i], "-1") != "-1"):
            checkSumTotal += int(vinDigitValues[vin[i]]) * vinDigitPositionMultiplier[i];
        else:
            #Characters not in the VinDigitValues list are not valid VIN characters - return false (invalid)
            print "Illegal Character: %s" % vin[i]
            return -1;

    remain = checkSumTotal % 11
    char = `remain`
    if remain == 10:
        char = 'X'

    return char
                
def getRandomVinChar():
    i = int(random.random() * len(vinDigitValues))
    return vinDigitValues.keys()[i]

def getRandomVinStart():
    #137DA903       T
    #137FA833       3
    vinFile = open("VinPrefixes.txt")
    count = 0

    # Get random Manufaturer and Model
    lineToRead = int(random.random() * 62178)

    try:
        while (count <= lineToRead):
            line = vinFile.readline()
            count += 1
    finally:
        vinFile.close()

    fields = line.split()
    return VinYear(fields[0].strip(), fields[1].strip())

def isValidVin(vin):
    #print("Vin Lenth: %s" % len(vin))
    if (len(vin) != 17):
            return False

    c = getCheckSumChar(vin)
    #print("Expected Character %s - Actual: %s" % (c, vin[8]))

    #9th character of the VIN is the Check Digit - if equal then valid
    return (c == vin[8]);

