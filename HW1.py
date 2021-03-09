# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107000212.csv'
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

#C0A880
target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
num = len(target_data)
lst_1=[]
for i in range(num):
    a = float(target_data[i]['HUMD'])
    lst_1.append(a) # adding the element 

if -99.000 in lst_1 or -999.000 in lst_1:
   lst1_out=['C0A880','NONE']
else:
   sum_1 = sum(lst_1)
   lst1_out=['C0A880',sum_1]


#C0F9A0
target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
num = len(target_data)
lst_2=[]
for i in range(num):
    a = float(target_data[i]['HUMD'])
    lst_2.append(a) # adding the element 

if -99.000 in lst_2 or -999.000 in lst_2:
   lst2_out=['C0F9A0','NONE']
else:
   sum_2 = sum(lst_2)
   lst2_out=['C0F9A0',sum_2]


#C0G640
target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
num = len(target_data)
lst_3=[]
for i in range(num):
    a = float(target_data[i]['HUMD'])
    lst_3.append(a) # adding the element 

if -99.000 in lst_3 or -999.000 in lst_3:
   lst3_out=['C0G640','NONE']
else:
   sum_3 = sum(lst_3)
   lst3_out=['C0G640',sum_3]


#C0R190
target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
num = len(target_data)
lst_4=[]
for i in range(num):
    a = float(target_data[i]['HUMD'])
    lst_4.append(a) # adding the element 

if -99.000 in lst_4 or -999.000 in lst_4:
   lst4_out=['C0R190','NONE']
else:
   sum_4 = sum(lst_4)
   lst4_out=['C0R190',sum_4]

#C0X260
target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
num = len(target_data)
lst_5=[]
for i in range(num):
    a = float(target_data[i]['HUMD'])
    lst_5.append(a) # adding the element 

if -99.000 in lst_5 or -999.000 in lst_5:
   lst5_out=['C0X260','NONE']
else:
   sum_5 = sum(lst_5)
   lst5_out=['C0X260',sum_5]
   
#=======================================

# Part. 4
#=======================================
# Print result
lst_result = [lst1_out,lst2_out,lst3_out,lst4_out,lst5_out]
print(lst_result)
#========================================