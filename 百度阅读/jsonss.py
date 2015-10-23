import json


f = file('setting.json')
print f
data = json.load(f)
print data['url']
