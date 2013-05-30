
import csv
import re


print">>>========================== \\\\ ==========================<<<"
print "  __________   __   ___       _ ______     ___ __  __         "
print " / ___/ __| | / /  / _ \___ _(_/ / _____  / (_/ /_/ /____ ____"
print "/ /___\ \ | |/ /  / , _/ _ `/ / _\ \/ _ \/ / / __/ __/ -_/ __/"
print "\___/___/ |___/  /_/|_|\_,_/_/_/___/ .__/_/_/\__/\__/\__/_/   "
print "                                  /_/                         "
print">>>========================== \\\\ ==========================<<<"



print "The splitter takes big CSV files and cuts them into littler, cuter ones."
print "NOTE: The splitter doesn't maintain the order of your files, so just give up. Also make sure you've got a header row."
print ""
print "Copy csv file as path and paste below."



csv_path = str(input("Where's your tuber? Full path (in quotes), please: ").strip('"'))

reader = csv.reader(open(csv_path, 'rU'))
lines = list(reader)

header_row=lines.pop(0)
print len(lines)

div_files = int(input("How many sticks you want? "))

it=1
for subset in [lines[i::div_files] for i in range(div_files)]:
	
	print "Splittin' file #"+str(it)

	write_path = re.sub(r'(\.csv)$',r'_sub'+str(it)+r'\1',csv_path)
	it+=1
	
	with open(write_path, 'wb') as writefile:
		writer = csv.writer(writefile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(header_row)
		for row in subset:
			writer.writerow(row)
print ""
print "All done. Now get along. You'll find your bundle in the same directory as your original."