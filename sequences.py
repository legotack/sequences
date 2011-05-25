class Test:
	def run(self, n):
		return n;

firstNums = raw_input("Please enter the first numbers of your sequence, separated by spaces: ").split(" ");
net = [[]];
for i in firstNums:
	net[0].append(float(i));
keepGoing = True;
while keepGoing:
	lastRow = len(net) - 1;
	net.append([]);
	for i in range(0, len(net[lastRow]) - 1):
		net[lastRow + 1].append(net[lastRow][i + 1] - net[lastRow][i]);
	try:
		if net[len(net) - 1][0] == net[len(net) - 1][1]:
			keepGoing = False;
	except IndexError:
		keepGoing = False;

length = int(raw_input("Please enter how many more numbers you would like to add to your sequence: "));
for i in range(len(net) - 1, -1, -1):
	for w in range(0, length):
		if i == len(net) - 1:
			net[i].append(net[i][0]);
		else:
			net[i].append(net[i][len(net[i]) - 1] + net[i + 1][len(net[i]) - 2]);

seeFull = raw_input("Would you like to see the whole net? (type \"Y or N\" (without the quotation marks)):");
outString = "";
if seeFull == "Y":
	for i in net:
		for w in i:
			outString += str(w) + ", ";
		outString += "\n";
else:
	for i in net[0]:
		outString += str(i) + ", ";

print outString;