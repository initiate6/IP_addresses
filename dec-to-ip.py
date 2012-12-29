#convert 10digit decimal formated ipaddress to normal ipaddress
#by init6
#blog.init6.me

import sys

def main():
    #read file and convert each line to ip address. Comment out to ask for input.
    #with open('c:\ipaddress.txt', 'r') as infile:
    #    for line in infile:
    #        print (convert(int(line)))
    #infile.close()

    #ask for input (dec format) Uncomment to ask for input.
    decIn = input("Enter 10 digit decimal formated ipaddress: ")
    print ( convert(decIn) )
    
def convert(decIn):

    if is32(decIn) == True:
        #convert dec to hex
        fullHex = hex(decIn).lstrip("0x")

        #Split hex number into four pairs
        hex1 = fullHex[0:2]
        hex2 = fullHex[2:4]
        hex3 = fullHex[4:6]
        hex4 = fullHex[6:8]
        #Convert each hex to decimal then to a string and return ip address.
        ipAddr = ( str(int(hex1,16)) + '.' + str(int(hex2,16)) + '.' + str(int(hex3,16)) + '.' + str(int(hex4,16)) )
        return ipAddr
    
#Checks to see if input is a 32bit int or less to make sure its a vaild ip address.         
def is32(n):
    try:
        bitstring=bin(n)
    except (TypeError, ValuueError):
        return False

    if len(bin(n)[2:]) <= 32:
        return True
    else:
        print ("Not a vaild 32bit 10 digit decimal")
        return False
    
main()
