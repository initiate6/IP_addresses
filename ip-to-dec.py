#convert ip address to a 10digit decimal formated ipaddress.
#by init6
#blog.init6.me

import sys

def main():
    ipAddr = raw_input("Type in IP Address to convert to 10digit decimal: ")
    print ( convert(ipAddr) )

def convert(ipAddr):
    out = ipAddr.split('.')
    octets = [int(out[0]), int(out[1]), int(out[2]), int(out[3])]
    hexNum = '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
    return int(hexNum, 16)

main()
