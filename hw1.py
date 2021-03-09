# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061142.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
#target_data = data[:10]
for i in data:
   if i['PRES'] == '-99.000' or i['PRES'] == '-999.000':
      i['PRES'] = '0'

s1 = 0
a1 = 0
s2 = 0
a2 = 0
s3 = 0
a3 = 0
s4 = 0
a4 = 0
s5 = 0
a5 = 0
for j in data:
   if j['station_id'] == 'C0A880' and j['PRES'] != '0':
      a1 = a1 + 1 
      s1 = s1 + float(j['PRES'])
   elif j['station_id'] == 'C0F9A0' and j['PRES'] != '0' :
      a2 = a2 + 1 
      s2 = s2 + float(j['PRES'])
   elif j['station_id'] == 'C0G640' and j['PRES'] != '0' :
      a3 = a3 + 1 
      s3 = s3 + float(j['PRES'])

   elif j['station_id'] == 'C0R190' and j['PRES'] != '0':
      a4 = a4 + 1 
      s4 = s4 + float(j['PRES'])

   elif j['station_id'] == 'C0X260':
      a5 = a5 + 1 
      s5 = s5 + float(j['PRES'])
mean1 = s1 / a1
mean2 = s2 / a2
mean3 = s3 / a3
mean4 = s4 / a4
mean5 = s5 / a5

alist = []

if mean1 == 0:
   alist.append(['C0A880', 'None'])
else: 
   alist.append(['C0A880', round(mean1, 2)])

if mean2 == 0:
   alist.append(['C0F9A0', 'None'])
else:
   alist.append(['C0F9A0', round(mean2, 2)])

if mean3 == 0:
   alist.append(['C0G640', 'None'])
else:
   alist.append(['C0G640', round(mean3, 2)])

if mean4 == 0:
   alist.append(['C0R190', 'None'])
else:
   alist.append(['C0R190', round(mean4, 2)])
if mean5 == 0:
   alist.append(['C0X260', 'None'])
else:
   alist.append(['C0X260', round(mean5, 2)])
print(alist)





#=======================================

# Part. 4
#=======================================
# Print result
#print(data)


#========================================