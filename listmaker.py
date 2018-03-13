import os, sys, datetime, random

#option to import seed from a file for backup purpose
if (len(sys.argv) == 2):
	seedfd = open(sys.argv[1], "r")
	name = seedfd.readline()
	random.seed(name)
	seedfd.close()
else:
	name = os.urandom(32)
	random.seed(name)
#open words list
wordlist = open("bip39.txt", "r")
#create and open output file
directory = "output/"
if not os.path.exists(directory):
    os.makedirs(directory)
datestr = str(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
loc = directory + datestr + ".txt"
fd = open (loc, "w")

arr = []
#we pick every word randomly, then we add them in the file and remove them from the list
for line in wordlist:
	arr.append(line.strip('\n'))
for i in range (0, 2048):
	if (i % 5 == 0 and i != 0):
		fd.write("\n")
	curword = random.randrange(0, 2048 - i)
	current = ("[%4d]%8s " % (i + 1, arr[curword]))
	arr.remove(arr[curword])
	fd.write(current)
#we back up the random seed
seedbackupfd = open(directory + "seed" + datestr +".txt" , "w")
seedbackupfd.write(name)
seedbackupfd.close()
fd.close()