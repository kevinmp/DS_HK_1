#!/usr/bin/python

"""
data file is ordered as "Age","Gender","Impressions","Clicks","Signed_In"
output csv report is ordered as: "age", "gender", "signed_in", "avg_click", "avg_impressions", "max_click", "max_impressions"
note: we are now aggregating into age, gender and signed in
side note: got tired of piping data, so reading file instead
"""

# open the data file for reading
datafile = open('data.csv', 'r')

# resultset stores [age, gender, signed_in, clicks. impressions, max clicks, max impressions, count]
resultset = [[0,0,0,0,0,0,0,1]]
# hack to skip first line
firstline = 1

for line in datafile:
	
	"""
	quick hack to skip the header.
	you could put in a try catch loop here at the top
	to test each data point to make sure it's valid and
	'continue' out of any invalid data in the stream but... nah.
	"""

	if firstline == 1:
		firstline = 0
		continue

	clean_line = line.strip().split(',')
	age = int(clean_line[0])
	gender =int(clean_line[1])
	impressions = int(clean_line[2])
	clicks = int(clean_line[3])
	signed_in = int(clean_line[4])
	data_matched = 0

	#print "Checking age: " + str(age) + ", gender: " + str(gender) + ", signed in: " +str(signed_in)
	#print "Result set size: " + str(len(resultset))
	for x in range(len(resultset)):
		#print "looping for: " + str(x) + " matched: " +str(data_matched)
		if resultset[x][0] == age and resultset[x][1] == gender and resultset[x][2] == signed_in:
			# yes, we found a match in the resultset, add up the line data
			data_matched = 1
			#increment resultset counter by 1
			resultset[x][7] += 1
			# clicks
			resultset[x][3] += clicks
			# impressions
			resultset[x][4] += impressions
			# max clicks
			if clicks >= resultset[x][5]:
				resultset[x][5] = clicks
			# max impressions
			if impressions >= resultset[x][6]:
				resultset[x][6] =  impressions

  	if not data_matched == 1:
  		# no matching resultset, add it to the resultset as a new data point
		resultset.append([age, gender, signed_in, clicks, impressions, clicks, impressions, 1])
datafile.close()

# tidy up the result set to make for easier reading
resultset.sort()

# open report file for writing
reportfile = open("report.txt", "w")
reportfile.write('"age", "gender", "signed_in", "avg_click", "avg_impressions", "max_click", "max_impressions"\n')
for item in resultset:
	# write age, gender and signed_in
	reportfile.write(str(item[0])+","+str(item[1])+","+str(item[2])+",")
	# write average clicks and impressions. use trick to float the values
	reportfile.write("%.4f,%.4f," % (float(item[3])/item[7],float(item[4])/item[7]))
	# write the max clicks and max impressions and newline
	reportfile.write(str(item[5])+","+str(item[6])+","+"\n")
reportfile.close()