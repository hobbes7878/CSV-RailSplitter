from __future__ import division
import csv
import re
import math



print">>>========================== \\\\ ==========================<<<"
print "  __________   __   ___       _ ______     ___ __  __         "
print " / ___/ __| | / /  / _ \___ _(_/ / _____  / (_/ /_/ /____ ____"
print "/ /___\ \ | |/ /  / , _/ _ `/ / _\ \/ _ \/ / / __/ __/ -_/ __/"
print "\___/___/ |___/  /_/|_|\_,_/_/_/___/ .__/_/_/\__/\__/\__/_/   "
print "                                  /_/                       2 "
print">>>========================== \\\\ ==========================<<<"


print "The splitter takes CSV files with fields larger than 250 chars and splits them into multiple fields."
print "NOTE: Make sure you've got a header row."
print ""
print "Copy csv file as path and paste below."


csv_path = str(input("Where's your timber? Full path (in quotes), please: "))
divid = int(input("Max field length? "))

reader = csv.reader(open(csv_path, 'rU'))
lines = list(reader)

header_row=lines.pop(0)
print len(lines)

csv_dicts=[]
for line in lines:
	row_dict=dict(zip(header_row,line))
	csv_dicts.append(row_dict)

longest=0

write_list=[]
key_list=[]


for csv_dict in csv_dicts:
	write_dict={}
	for key in csv_dict:
		key_list.append(key)
		write_dict[key]=unicode(csv_dict[key], errors='ignore')
		if len(csv_dict[key])>divid:
			if len(csv_dict[key])>longest:
				longest = len(csv_dict[key])
			parsable=csv_dict[key]
			splits=int(math.ceil(len(csv_dict[key])/divid))
			i=0
			for split in range(splits):
				write_dict[key+"_"+str(split+1)]=unicode(parsable[i:i+divid], errors='ignore')
				i+=divid
			write_dict[key]=""
	write_list.append(write_dict)

print longest

write_path = re.sub(r'(\.csv)$',r'_split'+r'\1',csv_path)
print write_path

with open(write_path,'wb') as writefile:
	all_keys=[k.keys() for k in write_list]
	writer=csv.DictWriter(writefile, set([key for sub_key_list in all_keys for key in sub_key_list]))
	writer.writeheader()
	writer.writerows(write_list)

### Check ###
for csv_dict in write_list:
	for key in csv_dict:
		if len(csv_dict[key])>divid:
			print "!!!! TOO LONG !!!"+str(len(csv_dict[key]))+str(key)
#############

print "All done now."