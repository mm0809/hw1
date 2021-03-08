# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061111.csv' #sample_input.csv or 108061111.csv
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

# List the target station_id in "lexicographical order"
station_id_list = ["C0A880", "C0F9A0", "C0G640", "C0R190", "C0X260"]

ans = []

for station_id in station_id_list:
    target_data = list(filter(lambda item: (item['station_id'] == station_id) and (item['PRES'] != '-99.000') and (item['PRES'] != '-999.000'), data))
    
    length = len(target_data)
    if(length != 0):
        average = sum(float(item['PRES']) for item in target_data) / length
    else:
        average = 'None'
        
    ans.append([station_id, average])

#=======================================

# Part. 4
#=======================================
# Output

# Because the ans being appended by lexicographical order, don't need to sort it again.
# ans.sort()
print(ans)
