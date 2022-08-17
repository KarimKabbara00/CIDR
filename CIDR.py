#splits the given input into each ip octet and the subnet
def parseIP(cidrNotation):
	addressSplit = cidrNotation.split('/')
	ip = addressSplit[0]
	cidrSubnet = addressSplit[1]
	
	ipSplit = ip.split('.')
	return (ipSplit, cidrSubnet)

#converts the / into a subnet. So /24 would be converted to the appropriate subnet which is 255.255.255.0
def convertCidrToDec(cidrSubnet):

	netmask = "" #netmask in binary
	for x in range (0, int(cidrSubnet)): #put 1s from 0 to 24
		netmask += str(1)
		
	for x in range (0, 32 - int(cidrSubnet)): #the rest is 0s
		netmask += str(0)

	#seperate the octets
	netmask1 = netmask2 = netmask3 = netmask4 = ""
	for x in range(0, 8):
		netmask1 += str(netmask[x])
	for x in range(8, 16):
		netmask2 += str(netmask[x])
	for x in range(16, 24):
		netmask3 += str(netmask[x])
	for x in range(24, 32):
		netmask4 += str(netmask[x])

        #convert the octets into ints
	netmask1 = str(int(netmask1, base = 2))
	netmask2 = str(int(netmask2, base = 2))
	netmask3 = str(int(netmask3, base = 2))
	netmask4 = str(int(netmask4, base = 2))
	return (netmask1, netmask2, netmask3, netmask4)
	
#uses the ip and its given subnet mask to print out the entire range of IPs available on the given subnet.
def printIPsInSubnet(ip, netmask):
	if int(netmask[2]) < 255:
		count3 = 255-int(netmask[2])
		for loop3 in range(0, count3):
			for loop4 in range (1, 256):
				print("{}.{}.{}.{}".format(ip[0], ip[1], loop3, loop4))
	elif int(netmask[3]) < 255:
		count4 = 255-int(netmask[3])
		for loop4 in range (1, count4):
			print("{}.{}.{}.{}".format(ip[0], ip[1], ip[2], loop4))


#main function to accept user input and put the functions above (and import) to use			
def main():
	print("Karim Kabbara, Python - CIDR Notation")
	cidrNotation = input("Enter your network in CIDR. e.g: 192.168.10.0/30: ")
	
	#I used try and except to catch any input that could crash the program.
	try:
		parseString = parseIP(cidrNotation)
		ip = parseString[0]
		cidrSubnet = parseString[1]
		print("\nIP:{}.{}.{}.{}\tCIDR:{}".format(ip[0], ip[1], ip[2], ip[3], cidrSubnet))
		
		netmask = convertCidrToDec(cidrSubnet)
		print("Subnet:{}.{}.{}.{}".format(netmask[0], netmask[1], netmask[2], netmask[3]))

		print("IPs in subnet:")
		printIPsInSubnet(ip, netmask)
		
	
	except:
		print("Invalid Input! Exiting...")
		
if __name__ == "__main__":
        main()
