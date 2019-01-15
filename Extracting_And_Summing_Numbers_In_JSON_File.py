import urllib.request, urllib.parse, urllib.error
import json

fhand = open('File.json')

data = ''

for line in fhand:
	input = line.rstrip()
	data = data + input

info = json.loads(data)
lst = info['comments']

total = 0

for item in lst:
	total = total + int(item['count'])
print('Total of Numbers in your JSON File is:', total)
