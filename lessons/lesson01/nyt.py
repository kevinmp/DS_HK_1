#!/usr/bin/python
# Import required libraries
import sys

# Start a counter and store the textfile in memory
count = 0
sum_ages = 0
sum_clicks = float(0)
clicks_list=[]
age_list=[]
oldest_person = [0,0,0,0,0]
lines = sys.stdin.readlines()
lines.pop(0)

# For each line, find the sum of index 2 in the list.
for line in lines:
  clean_line = line.strip().split(',')
  count = count + int(clean_line[2])
  sum_ages += int(clean_line[0])
  clicks_list.append(float(clean_line[3]))
  age_list.append(int(clean_line[0]))
  if int(clean_line[0]) > int(oldest_person[0]):
  	oldest_person = clean_line

print 'Impressions Sum:', count
print 'Clicks Sum:', sum(clicks_list) 			# print all total clicks
print 'CTR: %.2f%%' % (sum(clicks_list)/count * 100)	# print the CTR in percentage (round to 2 decimal points)
print 'Average Age:', sum_ages/len(lines)		# print the Average Age
print 'Max Age:', max(age_list)					# print the Max Age
print 'oldest_person', oldest_person


file = open("report.txt", "w")
file.write("Impressions Sum: " + str(count) + "\n")
file.write("Clicks Sum: " + str(sum(clicks_list)) + "\n")
file.write("CTR: %.2f%%" % (sum(clicks_list)/count * 100) + "\n")
file.write("Average Age: " + str(sum_ages/len(lines)) + "\n")
file.write("Max Age: " + str(max(age_list)) + "\n")
file.write("Oldest Person: " + str(oldest_person) + "\n") 
file.close()
