import os, sys, datetime, random

#option to allow seed setting for backup purpose
if (len(sys.argv) == 2):
	random.seed(sys.argv[1])
	print "i"
#open words list
wordlist = open("bip39.txt", "r")
#create output file
directory = "output"
if not os.path.exists(directory):
    os.makedirs(directory)
loc = directory + "/" + str(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')) + ".txt"
fd = open (loc, "w")
arr = []

for line in wordlist:
	arr.append(line.strip('\n'))
for i in range (0, 2048):
	if (i % 5 == 0 and i != 0):
		fd.write("\n")
	curword = random.randrange(0, 2047 - i + 1)
	current = ("[%4d]%8s " % (i + 1, arr[curword]))
	arr.remove(arr[curword])
	fd.write(current)