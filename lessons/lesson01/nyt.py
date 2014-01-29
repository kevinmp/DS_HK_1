#!/usr/bin/python
# Import required libraries
import sys

# Start a counter and store the textfile in memory
count = 0
sum_ages = 0
sum_clicks = float(0)
clicks_list=[]
age_list=[]
lines = sys.stdin.readlines()
lines.pop(0)

# For each line, find the sum of index 2 in the list.
for line in lines:
  count = count + int(line.strip().split(',')[2])
  sum_ages += int(line.strip().split(',')[0])
  sum_clicks += int(line.strip().split(',')[3])
  clicks_list.append(int(line.strip().split(',')[3]))
  age_list.append(int(line.strip().split(',')[0]))

print 'Impressions Sum:', count
print 'Clicks Sum:', sum(clicks_list) 			# print all total clicks
print 'CTR: %.2f%%' % (sum_clicks/count * 100)	# print the CTR in percentage (round to 2 decimal points)
print 'Average Age:', sum_ages/len(lines)		# print the Average Age
print 'Max Age:', max(age_list)					# print the Max Age

